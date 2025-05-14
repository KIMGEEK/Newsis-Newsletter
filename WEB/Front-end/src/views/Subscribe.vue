<template>
  <div class="subscribe-container">
    <h1>뉴스레터 구독하기</h1>
    <form @submit.prevent="handleSubmit" class="subscribe-form">
      <div class="form-group">
        <label for="email">이메일</label>
        <input 
          type="email" 
          id="email" 
          v-model="formData.email" 
          required
          placeholder="example@email.com"
        >
      </div>
      
      <div class="form-group">
        <label for="name">이름</label>
        <input 
          type="text" 
          id="name" 
          v-model="formData.name" 
          required
          placeholder="홍길동"
        >
      </div>
      
      <div class="form-group">
        <label>구독 카테고리</label>
        <div class="checkbox-group">
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="formData.categories" 
              value="frontend"
            >
            프론트엔드
          </label>
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="formData.categories" 
              value="backend"
            >
            백엔드
          </label>
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="formData.categories" 
              value="ai"
            >
            AI
          </label>
        </div>
      </div>

      <button type="submit" class="submit-btn">구독하기</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'Subscribe',
  data() {
    return {
      formData: {
        email: '',
        name: '',
        categories: []
      }
    }
  },
  methods: {
    handleSubmit() {
      // TODO: 실제 구독 처리 로직 구현
      console.log('구독 정보:', this.formData)
      alert('구독이 완료되었습니다!')
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
.subscribe-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 32px;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px #0001;
}

h1 {
  text-align: center;
  margin-bottom: 32px;
  color: #333;
}

.subscribe-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

label {
  font-weight: bold;
  color: #444;
}

input[type="email"],
input[type="text"] {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 16px;
}

.checkbox-group {
  display: flex;
  gap: 24px;
  margin-top: 8px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.submit-btn {
  background: #42b983;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-btn:hover {
  background: #3aa876;
}
</style> 