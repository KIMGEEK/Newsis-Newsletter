import { computed, ref, onMounted } from 'vue'
import axios from 'axios';
import { BASE_URL, MEDIA_BASE_URL } from './NewsletterList.js';

// 이미지 컴포넌트
const NewsletterImage = {
  name: 'NewsletterImage',
  props: {
    imageSrc: {
      type: String,
      required: true
    }
  },
  template: `
    <div class="image-zoom-wrapper">
      <img
        class="detail-image"
        :src="imageSrc"
        :alt="'뉴스레터 이미지'"
        @error="handleImageError"
        @load="handleImageLoad"
      />
      <p v-if="imageError" class="image-error">이미지를 불러올 수 없습니다</p>
    </div>
  `,
  data() {
    return {
      imageError: false
    }
  },
  methods: {
    handleImageError(e) {
      console.error('이미지 로드 실패:', this.imageSrc);
      this.imageError = true;
    },
    handleImageLoad() {
      console.log('이미지 로드 성공:', this.imageSrc);
      this.imageError = false;
    }
  }
}

// 참고 링크 컴포넌트
const ReferenceLinks = {
  name: 'ReferenceLinks',
  props: {
    links: {
      type: Array,
      required: true
    }
  },
  template: `
    <div class="reference-list">
      <h3>참고 링크</h3>
      <ul>
        <li v-for="(link, i) in links" :key="i">
          <a :href="link" target="_blank">{{ link }}</a>
        </li>
      </ul>
    </div>
  `
}

export default {
  name: 'NewsletterDetail',
  components: {
    NewsletterImage,
    ReferenceLinks
  },
  props: ['id'],
  setup(props) {
    const newsletters = ref([]);
    const loading = ref(true);
    const error = ref(null);

    const fetchNewsletter = async () => {
      try {
        loading.value = true;
        const response = await axios.get(`${BASE_URL}?weeks=${props.id}`);
        newsletters.value = response.data.map(item => {
          const newsData = JSON.parse(item.news.replace(/'/g, '"'));
          // 항상 이미지 URL을 생성
          const imageUrl = `${MEDIA_BASE_URL}${item.weeks}/${item.index}.png`;
          return {
            ...newsData,
            image: imageUrl
          };
        });
        loading.value = false;
      } catch (err) {
        error.value = '뉴스레터를 불러오는데 실패했습니다';
        loading.value = false;
        console.error('Error fetching newsletter:', err);
      }
    };

    onMounted(() => {
      fetchNewsletter();
    });

    return {
      newsletters,
      loading,
      error
    }
  }
} 