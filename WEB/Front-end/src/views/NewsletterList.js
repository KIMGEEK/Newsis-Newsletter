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