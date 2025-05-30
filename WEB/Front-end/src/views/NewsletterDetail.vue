<template>
  <div class="newsletter-detail">
    <!-- 상단 네비게이션 -->
    <router-link to="/" class="back-link">← 목록으로</router-link>

    <!-- 뉴스레터 내용 -->
    <section v-for="(item, idx) in currentNewsletter" :key="idx" class="newsletter-item">
      <h1>{{ item.date || '최신 뉴스레터' }}</h1>
      <NewsletterImage 
        :image-src="item.image"
      />
      <h2 class="title">{{ item.title }}</h2>
      <div class="content">{{ item.text }}</div>
      <ReferenceLinks v-if="item.reference" :links="item.reference" />
      <hr v-if="idx < currentNewsletter.length - 1" />
    </section>

    <!-- 구독 섹션 -->
    <section class="subscribe-section">
      <p class="subscribe-text">우리의 소식을 더 듣고 싶다면 아래의 구독하기를 클릭해주세요</p>
      <router-link to="/subscribe" class="subscribe-link">구독하기</router-link>
    </section>

    <!-- 하단 네비게이션 -->
    <router-link to="/" class="back-link">← 목록으로</router-link>
  </div>
</template>

<script>
import { computed } from 'vue'
import newsletters from '../assets/프론트엔드.json'
import newsletters2 from '../assets/프론트엔드 copy.json'

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
        :src="'/src/assets/' + imageSrc"
        :alt="'뉴스레터 이미지: ' + imageSrc"
        @error="handleImageError"
        @load="handleImageLoad"
      />
      <p v-if="imageError" class="image-error">이미지를 불러올 수 없습니다: {{ imageSrc }}</p>
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
    const allNewsletters = [newsletters, newsletters2]
    const currentNewsletter = computed(() => {
      return allNewsletters[Number(props.id)]
    })

    return { 
      currentNewsletter
    }
  }
}
</script>

<style scoped>
/* 전체 레이아웃 */
.newsletter-detail {
  max-width: 900px;
  margin: 40px auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0001;
  padding: 32px;
  box-sizing: border-box;
}

.newsletter-item {
  margin-bottom: 48px;
}

/* 이미지 스타일 */
:deep(.image-zoom-wrapper) {
  width: 100%;
  max-width: 300px;
  margin: 24px auto;
  border-radius: 8px;
  background: #f5f5f5;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
}

:deep(.detail-image) {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
  max-width: 100%;
  max-height: 300px;
}

/* 텍스트 스타일 */
.content {
  font-size: 17px;
  line-height: 1.7;
  color: #222;
  margin-bottom: 32px;
}

/* 참고 링크 스타일 */
.reference-list {
  margin-bottom: 32px;
}

.reference-list ul {
  padding-left: 18px;
}

.reference-list a {
  color: #1976d2;
  text-decoration: underline;
  font-size: 15px;
}

/* 네비게이션 링크 */
.back-link {
  color: #e55;
  text-decoration: none;
  font-weight: bold;
}

/* 구독 섹션 */
.subscribe-section {
  margin: 48px 0;
  padding: 24px;
  background: #f8f9fa;
  border-radius: 12px;
  text-align: center;
}

.subscribe-text {
  margin-bottom: 16px;
  color: #666;
  font-size: 16px;
}

.subscribe-link {
  display: inline-block;
  background: #42b983;
  color: white;
  padding: 12px 32px;
  border-radius: 6px;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.2s;
}

.subscribe-link:hover {
  background: #3aa876;
}
</style> 