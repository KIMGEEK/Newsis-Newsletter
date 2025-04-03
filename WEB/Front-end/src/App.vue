<template>
  <PageHeader />
  <!-- 헤더 컴포넌트 -->
  <router-view />
  <!-- 페이지 이동이 표시될 곳 -->
  <PageFooter />
  <!-- 푸터 컴포넌트 -->
</template>

<script>
import PageHeader from "./components/PageHeader.vue";
import PageFooter from "./components/PageFooter.vue";

export default {
  name: "App",
  components: {
    PageFooter,
    PageHeader,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: flex;
  flex-direction: column;
}

.app-container {
  min-height: 1280vh;
  margin:0 auto;
  width: 100%;
  padding: 2rem;
}

.main-content {
  flex: 1;
  padding: 2rem 0;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
  margin: 0 10px;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>