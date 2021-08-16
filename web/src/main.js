import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false
Vue.prototype.$endpoint = process.env.VUE_APP_ENDPOINT;
new Vue({
  render: h => h(App),
}).$mount('#app')
