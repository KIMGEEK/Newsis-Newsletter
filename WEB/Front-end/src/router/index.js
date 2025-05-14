import { createRouter, createWebHistory } from "vue-router";
import NewsletterList from '../views/NewsletterList.vue';
import NewsletterDetail from '../views/NewsletterDetail.vue';
import Subscribe from '../views/Subscribe.vue';

const routes = [
  {
    path: "/",
    name: "NewsletterList",
    component: NewsletterList,
  },
  {
    path: "/newsletter",
    name: "NewsletterListAlias",
    component: NewsletterList,
  },
  {
    path: "/newsletter/:id",
    name: "NewsletterDetail",
    component: NewsletterDetail,
    props: true,
  },
  {
    path: "/subscribe",
    name: "Subscribe",
    component: Subscribe,
  },
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
