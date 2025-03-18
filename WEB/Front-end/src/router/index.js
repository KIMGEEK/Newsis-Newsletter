import { createRouter, createWebHistory } from "vue-router";
import PageHome from "../views/PageHome.vue";
import PageAbout from "../views/PageAbout.vue";
import BoardList from "../views/board/BoardList.vue";

const routes = [
  {
    path: "/",
    name: "PageHome",
    component: PageHome,
  },
  {
    path: "/about",
    name: "About",
    component: PageAbout,
  },
  {
    path: "/board/list",
    name: "Board",
    component: BoardList,
  },
];

const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
