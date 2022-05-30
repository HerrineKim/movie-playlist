<template>
  <div class="widget home container">
    <div style="width: auto; height: 50px;">
    </div>
    <div class="pb-5">
      <header-text></header-text>
    </div>
    <div class="row row-cols-2">
      <div style="margin-top:61px;" class="col py-5 px-3 boxof">
        <div class="mx-5">
          <boxoffice-kor></boxoffice-kor>
        </div>
      </div>
      <div class="col py-5 px-3 mt-3">
        <random-ost></random-ost>
      </div>
      <div class="col py-3 boxquote">
        <div>
          <random-quotes></random-quotes>
        </div>
      </div>
      <div 
      class="col boxactor">
        <div class="row row-col-2">
          <div class="col">
            <random-actor></random-actor>
          </div>
          <div style="
          color: #999999;
          font-family:MapoGoldenPier; 
          font-size:30px; text-align:left;
          padding-top: 30px;
          padding-left:50px;" class="col">
            <p style="line-height:10px">배우들을</p>
            <p>만나보세요</p>
          </div>
        </div>
      </div>
    </div>
    <div style="width: auto; height: 100px;">
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from "vuex"
import BoxofficeKor from "@/components/molecules/Home/BoxofficeKor.vue"
import RandomQuotes from '@/components/molecules/Home/RandomQuotes.vue'
import RandomActor from '@/components/molecules/Home/RandomActor.vue'
import RandomOst from '@/components/molecules/Home/RandomOst.vue'
import HeaderText from '@/components/molecules/Home/HeaderText.vue'

export default {
  name: 'WidgetsOrganism',
  components: {
    BoxofficeKor,
    RandomQuotes,
    RandomActor,
    RandomOst,
    HeaderText
  },
  computed: {
    ...mapGetters([
      'boxoffice'
    ]),
  },
}
</script>

<style scoped>
.boxof {
    background: linear-gradient(140deg, #005aa7, #fffde4 100%);
    border-radius: 30px;
    width: 500px;
    height: 400px
}

.boxquote {
    background: #ffff;
    border-radius: 30px;
    width: 500px;
    height: 400px
}

.boxactor {
  border:1px;
  border-radius: 30px;
  width: 500px;
  height: 400px;
  margin-left: 65px;
}
.txt {
  text-align: left;
  position: fixed;
  bottom: 240px;
  right: -200px;
}
.widget  {
  /* background-image:url(@/assets/images/MusicNote.png); */
  background-repeat: no-repeat;
  background-position: center top;

}
</style>