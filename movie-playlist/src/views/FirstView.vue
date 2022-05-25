<template>
  <div class="first">
    <nav-bar></nav-bar>
    <h2>로그인 시 보여주는 명대사 초기화면 (vue transition 사용)</h2>
    <div v-if="byeData" @click="bye">
      <letter-quote></letter-quote>      
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import router from "@/router"
import LetterQuote from "@/components/organisms/First/LetterQuote.vue"
export default {
  name: 'FirstView',
  components: {
    LetterQuote, NavBar
  },
  data() {
    return {
      byeData: true
    }
  },
  methods: {
    bye: function () {
      router.push({ name: "HomeView" })
    }
  },
}
</script>

<style>

</style>