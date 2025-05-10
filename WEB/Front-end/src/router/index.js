import { createRouter, createWebHistory } from "vue-router";
import NewsletterList from '../views/NewsletterList.vue';
import NewsletterDetail from '../views/NewsletterDetail.vue';

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
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
