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
          @input="validateEmail"
        >
        <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
      </div>
      
      <div class="form-group">
        <label for="name">이름</label>
        <input 
          type="text" 
          id="name" 
          v-model="formData.name" 
          required
          placeholder="홍길동"
          @input="validateName"
        >
        <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
      </div>
      
      <div class="form-group">
        <label>구독 카테고리</label>
        <div class="checkbox-group">
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="formData.categories" 
              value="web"
            >
            웹
          </label>
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="formData.categories" 
              value="ai"
            >
            AI
          </label>
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="formData.categories" 
              value="game"
            >
            게임
          </label>
        </div>
        <span v-if="errors.categories" class="error-message">{{ errors.categories }}</span>
      </div>

      <button type="submit" class="submit-btn" :disabled="isSubmitting">
        {{ isSubmitting ? '처리중...' : '구독하기' }}
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
let url = "http://localhost:8000/subscribe/";

export default {
  name: 'Subscribe',
  data() {
    return {
      formData: {
        email: '',
        name: '',
        categories: []
      },
      errors: {
        email: '',
        name: '',
        categories: ''
      },
      isSubmitting: false
    }
  },
  methods: {
    validateEmail() {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      if (!this.formData.email) {
        this.errors.email = '이메일을 입력해주세요.'
      } else if (!emailRegex.test(this.formData.email)) {
        this.errors.email = '올바른 이메일 형식이 아닙니다.'
      } else {
        this.errors.email = ''
      }
    },
    validateName() {
      if (!this.formData.name) {
        this.errors.name = '이름을 입력해주세요.'
      } else if (this.formData.name.length < 2) {
        this.errors.name = '이름은 2글자 이상이어야 합니다.'
      } else {
        this.errors.name = ''
      }
    },
    validateCategories() {
      if (this.formData.categories.length === 0) {
        this.errors.categories = '최소 하나의 카테고리를 선택해주세요.'
        return false
      }
      this.errors.categories = ''
      return true
    },
    async handleSubmit() {
      try {
        // 입력값 검증
        this.validateEmail()
        this.validateName()
        const isCategoriesValid = this.validateCategories()

        if (this.errors.email || this.errors.name || !isCategoriesValid) {
          return
        }

        this.isSubmitting = true

        // TODO: 실제 구독 처리 로직 구현
        // 예시: API 호출
        //await axios.post('http://localhost:8000/subscribe', this.formData)

        axios({
          method: "POST",
          url: url,
          data: this.formData,
        })
          .then((response) => {
            console.log(response.data);
          })
          .catch((error) => {
            console.log("Failed to create:", error.response);
          });
        
        // 임시 처리
        //await new Promise(resolve => setTimeout(resolve, 1000))
        //console.log('구독 정보:', this.formData)
        
        alert('구독이 완료되었습니다!')
        this.$router.push('/')
      } catch (error) {
        console.error('구독 처리 중 오류 발생:', error)
        alert('구독 처리 중 오류가 발생했습니다. 다시 시도해주세요.')
      } finally {
        this.isSubmitting = false
      }
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

input[type="email"]:focus,
input[type="text"]:focus {
  outline: none;
  border-color: #42b983;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.1);
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

.error-message {
  color: #dc3545;
  font-size: 14px;
  margin-top: 4px;
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

.submit-btn:hover:not(:disabled) {
  background: #3aa876;
}

.submit-btn:disabled {
  background: #a8d5c3;
  cursor: not-allowed;
}
</style> 