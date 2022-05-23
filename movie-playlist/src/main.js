import Vue from 'vue'

import VueGeolocationApi from 'vue-geolocation-api'
import VueCookies from 'vue-cookies'
import lodash from 'lodash'

import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false

Vue.use(VueGeolocationApi, lodash, VueCookies)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
