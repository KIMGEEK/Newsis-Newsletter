<template>
  <div v-if="newsletters && newsletters.length > 0" class="newsletter-detail">
    <!-- 상단 네비게이션 -->
    <router-link to="/" class="back-link">← 목록으로</router-link>

    <!-- 뉴스레터 목록 -->
    <section v-for="(item, idx) in newsletters" :key="idx" 
             :class="['newsletter-item', { 'main-newsletter': idx === 0 }]">
      <h1 v-if="idx === 0">{{ item.date }}</h1>
      <NewsletterImage 
        :image-src="item.image"
        :ref="el => { if (el) newsletterImages[idx] = el }"
      />
      <h2 class="title">{{ item.title }}</h2>
      <div class="content">{{ item.text }}</div>
      <ReferenceLinks v-if="item.reference" :links="item.reference" />
      <hr v-if="idx < newsletters.length - 1" />
    </section>

    <!-- 구독 섹션 -->
    <section class="subscribe-section">
      <p class="subscribe-text">우리의 소식을 더 듣고 싶다면 아래의 구독하기를 클릭해주세요</p>
      <router-link to="/subscribe" class="subscribe-link">구독하기</router-link>
    </section>

    <!-- 하단 네비게이션 -->
    <router-link to="/" class="back-link">← 목록으로</router-link>
  </div>
  <div v-else class="newsletter-detail">
    <p>뉴스레터를 찾을 수 없습니다.</p>
    <router-link to="/" class="back-link">← 목록으로</router-link>
  </div>
</template>

<script>
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import newsletterData from '../assets/프론트엔드.json'

// 이미지 컴포넌트
const NewsletterImage = {
  name: 'NewsletterImage',
  props: {
    imageSrc: {
      type: String,
      required: true
    }
  },
  setup(props, { expose }) {
    const imageRef = ref(null)
    
    expose({
      getImageElement: () => imageRef.value
    })

    return {
      imageRef
    }
  },
  template: `
    <div class="image-zoom-wrapper">
      <img
        ref="imageRef"
        class="detail-image"
        :src="'/src/assets/' + imageSrc"
        alt="본문 이미지"
      />
    </div>
  `
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
  props: {
    id: {
      type: [String, Number],
      required: true
    }
  },
  setup(props) {
    const newsletterImages = ref([])

    // 현재 뉴스레터를 첫 번째로, 나머지를 그 뒤로 정렬
    const newsletters = computed(() => {
      if (!newsletterData || !Array.isArray(newsletterData)) {
        return []
      }

      const currentId = Number(props.id)
      if (isNaN(currentId) || currentId < 0 || currentId >= newsletterData.length) {
        return []
      }

      const currentNewsletter = newsletterData[currentId]
      const otherNews = newsletterData.filter((_, idx) => idx !== currentId)
      return [currentNewsletter, ...otherNews]
    })

    // 이미지 확대 효과 계산 함수
    const calculateZoom = (rect, windowHeight) => {
      if (!rect) return 'scale(1)'
      if (rect.top < windowHeight && rect.bottom > 0) {
        const visible = Math.min(1, Math.max(0, 1 - rect.top / windowHeight))
        return `scale(${1 + visible * 0.2})`
      }
      return 'scale(1)'
    }

    // 스크롤 이벤트 핸들러
    const handleScroll = () => {
      if (!newsletterImages.value) return
      
      const images = newsletterImages.value
      const windowHeight = window.innerHeight

      images.forEach(img => {
        if (!img) return
        const imageElement = img.getImageElement()
        if (!imageElement) return
        const rect = imageElement.getBoundingClientRect()
        imageElement.style.transform = calculateZoom(rect, windowHeight)
      })
    }

    // 컴포넌트 마운트/언마운트 시 이벤트 리스너 설정/제거
    onMounted(() => {
      window.addEventListener('scroll', handleScroll)
    })
    onBeforeUnmount(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    return { 
      newsletters,
      newsletterImages
    }
  }
}
</script>

<style scoped>
/* 전체 레이아웃 */
.newsletter-detail {
  max-width: 700px;
  margin: 40px auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0001;
  padding: 32px;
}

/* 뉴스레터 아이템 스타일 */
.newsletter-item {
  margin-bottom: 48px;
}

.main-newsletter {
  margin-bottom: 64px;
}

/* 이미지 스타일 */
.image-zoom-wrapper {
  width: 100%;
  overflow: hidden;
  margin: 24px 0;
  border-radius: 8px;
}

.detail-image {
  width: 100%;
  max-height: 350px;
  object-fit: cover;
  transition: transform 0.4s cubic-bezier(0.4,0,0.2,1);
  will-change: transform;
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