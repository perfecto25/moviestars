<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/80s.jpeg">
    <MovieStar/>
  </div>
</template>

<script>
import MovieStar from './components/MovieStar.vue'

export default {
  name: 'App',
  components: {
    MovieStar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
