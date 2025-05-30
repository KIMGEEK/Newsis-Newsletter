import newsletters from '../assets/프론트엔드.json'
import newsletters2 from '../assets/프론트엔드 copy.json'
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:9000/post/'

export default {
  name: 'NewsletterList',
  computed: {
    newsletterPreviews() {
      return [
        newsletters[0],  // 첫 번째 게시글의 첫 번째 데이터
        newsletters2[0]  // 두 번째 게시글의 첫 번째 데이터
      ]
    }
  },
  methods: {
    goToDetail(idx) {
      this.$router.push(`/newsletter/${idx}`)
    }
  }
} 