import axios from 'axios';

export const BASE_URL = 'http://203.255.81.76:24040/post/';
export const MEDIA_BASE_URL = 'http://203.255.81.76:24040/media/';

export default {
  name: 'NewsletterList',
  data() {
    return {
      newsletters: [],
      loading: true,
      error: null
    }
  },
  async created() {
    try {
      const response = await axios.get(BASE_URL);
      this.newsletters = response.data;
      this.loading = false;
    } catch (err) {
      this.error = 'Failed to fetch newsletters';
      this.loading = false;
      console.error('Error fetching newsletters:', err);
    }
  },
  computed: {
    newsletterPreviews() {
      return this.newsletters.map(week => ({
        ...week.news[0],
        week: week.weeks,
        imageUrl: `${MEDIA_BASE_URL}${week.weeks}/${week.index}.png`
      }));
    }
  },
  methods: {
    goToDetail(week) {
      this.$router.push(`/newsletter/${week}`);
    }
  }
} 