<template>
  <div class="moviestar">
    <h1 v-if="vue_env=='dev'">80s Movie Stars (DEVELOPMENT)</h1>
    <h1 v-else>80s Movie Stars (PRODUCTION)</h1>
    
    <br>
    <button @click="fetch_stars()">Click to fetch</button>
    <br><br>

    <div align="center" v-if="moviestars">
      <table>
        <tr>
          <th>Name</th>
          <th>Movies</th>
        </tr>
        <tr v-for="(star, name) in moviestars" :key="name">
          <td>{{name}}</td>
          <td><li v-for="movie in star.movies" :key="movie">{{movie}}</li></td>
        </tr>
      </table>
    </div>

    <br>
    
    <button v-if="moviestars" @click="moviestars=null">Clear</button>
    

  </div>
</template>

<script>
export default {
  name: 'MovieStar',
  data() {
    return {
      moviestars: '',
      vue_env: process.env.VUE_APP_ENV,
    }
  },

  methods : {

     // fetch movie stars from python API
    fetch_stars(){
      fetch(this.$endpoint + "/fetch")
      .then(async response => {
        const apidata = await response.json();
        this.moviestars = apidata;
        this.errorMessage = false;
      })
      .catch(error => {
        this.errorMessage = error;
        console.error(error);
      });
    },
  }
}
</script>

<style>
  table, th, td { border: 1px solid black; padding:5px }
</style>
