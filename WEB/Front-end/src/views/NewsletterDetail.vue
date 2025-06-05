<script>
import NewsletterDetail from './NewsletterDetail.js'
export default NewsletterDetail
</script>

<template>
  <div class="newsletter-detail">
    <!-- 상단 네비게이션 -->
    <router-link to="/" class="back-link">← 목록으로</router-link>

    <!-- 로딩 상태 -->
    <div v-if="loading" class="loading-state">
      뉴스레터를 불러오는 중...
    </div>

    <!-- 에러 상태 -->
    <div v-else-if="error" class="error-state">
      {{ error }}
    </div>

    <!-- 뉴스레터 내용 -->
    <template v-else>
      <section v-for="(item, idx) in newsletters" :key="idx" class="newsletter-item">
        <h1>{{ item.title }}</h1>
        <NewsletterImage 
          v-if="item.image"
          :image-src="item.image"
        />
        <div class="content">{{ item.text }}</div>
        <ReferenceLinks v-if="item.reference" :links="item.reference" />
        <hr v-if="idx < newsletters.length - 1" />
      </section>
    </template>

    <!-- 구독 섹션 -->
    <section class="subscribe-section">
      <p class="subscribe-text">우리의 소식을 더 듣고 싶다면 아래의 구독하기를 클릭해주세요</p>
      <router-link to="/subscribe" class="subscribe-link">구독하기</router-link>
    </section>

    <!-- 하단 네비게이션 -->
    <router-link to="/" class="back-link">← 목록으로</router-link>
  </div>
</template>

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

/* 로딩 및 에러 상태 */
.loading-state,
.error-state {
  text-align: center;
  padding: 40px;
  color: #666;
  font-size: 18px;
}

.error-state {
  color: #e55;
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