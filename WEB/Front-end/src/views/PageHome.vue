<!-- PageHome.vue -->
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.svg" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "../components/HelloWorld.vue";

export default {
  name: "PageHome",
  components: {
    HelloWorld,
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}
img {
  width: 200px;
  height: auto;
  margin-bottom: 2rem;
}
</style>