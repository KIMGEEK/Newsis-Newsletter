<template>
  <div v-if="newsletter" class="newsletter-detail">
    <router-link to="/" class="back-link">← 목록으로</router-link>
    <h1>{{ newsletter.title }}</h1>
    <div class="image-zoom-wrapper">
      <img
        ref="detailImage"
        class="detail-image"
        :src="`/src/assets/${newsletter.image}`"
        alt="본문 이미지"
      />
    </div>
    <div class="content">{{ newsletter.text }}</div>
    <div v-if="newsletter.reference && newsletter.reference.length" class="reference-list">
      <h3>참고 링크</h3>
      <ul>
        <li v-for="(ref, i) in newsletter.reference" :key="i">
          <a :href="ref" target="_blank">{{ ref }}</a>
        </li>
      </ul>
    </div>
    <!-- 나머지 게시글들 -->
    <div v-for="(item, idx) in otherNews" :key="idx" class="other-news">
      <hr />
      <div class="image-zoom-wrapper">
        <img
          class="detail-image"
          :src="`/src/assets/${item.image}`"
          alt="본문 이미지"
        />
      </div>
      <div class="content">{{ item.text }}</div>
      <div v-if="item.reference && item.reference.length" class="reference-list">
        <h3>참고 링크</h3>
        <ul>
          <li v-for="(ref, i) in item.reference" :key="i">
            <a :href="ref" target="_blank">{{ ref }}</a>
          </li>
        </ul>
      </div>
    </div>
    <router-link to="/" class="back-link">← 목록으로</router-link>
  </div>
  <div v-else>
    <p>뉴스레터를 찾을 수 없습니다.</p>
  </div>
</template>

<script>
import { onMounted, onBeforeUnmount, ref, computed } from 'vue'
import newsletters from '../assets/프론트엔드.json'

export default {
  name: 'NewsletterDetail',
  props: ['id'],
  setup(props) {
    const newsletter = newsletters[Number(props.id)]
    const detailImage = ref(null)
    const otherNews = computed(() => newsletters.filter((_, idx) => idx !== Number(props.id)))

    // 스크롤에 따라 이미지 확대
    const handleScroll = () => {
      const img = detailImage.value
      if (!img) return
      const rect = img.getBoundingClientRect()
      const windowHeight = window.innerHeight
      if (rect.top < windowHeight && rect.bottom > 0) {
        // 스크롤 비율 계산 (0~1)
        const visible = Math.min(1, Math.max(0, 1 - rect.top / windowHeight))
        img.style.transform = `scale(${1 + visible * 0.2})`
      } else {
        img.style.transform = 'scale(1)'
      }
    }

    onMounted(() => {
      window.addEventListener('scroll', handleScroll)
    })
    onBeforeUnmount(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    return { newsletter, detailImage, otherNews }
  }
}
</script>

<style scoped>
.newsletter-detail {
  max-width: 700px;
  margin: 40px auto;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0001;
  padding: 32px;
}
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
.content {
  font-size: 17px;
  line-height: 1.7;
  color: #222;
  margin-bottom: 32px;
}
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
.back-link {
  color: #e55;
  text-decoration: none;
  font-weight: bold;
}
.other-news {
  margin-top: 48px;
}
</style> 