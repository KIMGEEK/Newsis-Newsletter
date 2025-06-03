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
      await axios.get(BASE_URL).then(response => {
        this.newsletters = response.data;
        this.loading = false;
        console.log('Processed newsletters:', this.newsletters);
      });
    } catch (err) {
      this.error = 'Failed to fetch newsletters';
      this.loading = false;
      console.error('Error fetching newsletters:', err);
    }
  },
  computed: {
    newsletterPreviews() {
      return this.newsletters.map(week => {
        const newsData = JSON.parse(week.news.replace(/'/g, '"'));
        console.log(newsData);
        return {
          news: week.news,
          week: this.getFormattedWeek(week.weeks),
          title: newsData.title,
          text: newsData.text,
          imageUrl: `${MEDIA_BASE_URL}${week.weeks}/${week.index}.png`
        };
      });
    }
  },
  methods: {
    goToDetail(week) {
      this.$router.push(`/newsletter/${week}`);
    },
    getFormattedWeek(week) {
      const parts = week.split('-');
      return `${parts[0]}년 ${parts[1]}월 ${parts[2]}주차`;
    }
  }
} 