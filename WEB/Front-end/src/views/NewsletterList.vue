<template>
  <div class="newsletter-list">
    <div
      v-if="newsPreview"
      class="newsletter-card"
      @click="goToDetail(0)"
    >
      <div class="thumbnail-wrapper">
        <img
          class="thumbnail"
          :src="`/src/assets/${newsPreview.image}`"
          alt="썸네일"
        />
        <div class="preview-slide">
          <p>{{ newsPreview.text.slice(0, 50) }}...</p>
        </div>
      </div>
      <div class="card-content">
        <h2>{{ newsPreview.title }}</h2>
      </div>
    </div>
  </div>
</template>

<script>
import newsletters from '../assets/프론트엔드.json'

export default {
  name: 'NewsletterList',
  computed: {
    newsPreview() {
      return newsletters[0]
    }
  },
  methods: {
    goToDetail(idx) {
      this.$router.push(`/newsletter/${idx}`)
    }
  }
}
</script>

<style scoped>
.newsletter-list {
  display: flex;
  flex-wrap: wrap;
  gap: 24px;
  justify-content: center;
}
.newsletter-card {
  width: 320px;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0001;
  background: #fff;
  cursor: pointer;
  overflow: hidden;
  transition: box-shadow 0.2s;
  position: relative;
  display: flex;
  flex-direction: column;
}
.newsletter-card:hover {
  box-shadow: 0 4px 16px #0002;
}
.thumbnail-wrapper {
  position: relative;
  width: 100%;
  height: 180px;
  overflow: hidden;
}
.thumbnail {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.preview-slide {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255,255,255,0.95);
  color: #333;
  padding: 16px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.4s cubic-bezier(0.4,0,0.2,1), padding 0.4s;
  box-sizing: border-box;
  z-index: 2;
}
.newsletter-card:hover .preview-slide {
  max-height: 120px;
  padding: 16px;
}
.card-content {
  padding: 16px;
}
</style> 