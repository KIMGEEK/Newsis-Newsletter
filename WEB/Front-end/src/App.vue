<template>
  <div id="app">
    <nav id="nav">
      <router-link to="/">뉴스레터</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
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
  background: #fff;
  border-bottom: 1px solid #eee;
  margin-bottom: 24px;
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