<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container mt-5">
      <div class="">
        <p style="font-size:40px; font-family:EarlyFontDiary;">커뮤니티</p>
      </div>
      <table class="table mt-5">
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col" style="text-align:left;font-family:GimpoGothicBold00;">글쓴이</th>
            <th scope="col" style="text-align:left;font-family:GimpoGothicBold00;">제목</th>
            <th scope="col" style="font-family:GimpoGothicBold00;">등록일</th>
            <th scope="col" style="font-family:GimpoGothicBold00;">좋아요</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="article in articles" :key="article.pk">
            <th scope="row" style="font-family: 'GmarketSansMedium';">{{ article.pk }}</th>
            <td style="text-align:left; font-family: 'GmarketSansMedium';">
              <router-link class="link" :to="{ name: 'profile', params: { username: article.user.username} }">
                {{ article.user.username }}
              </router-link>
            </td>
            <td style="font-family: 'GmarketSansMedium'; text-align: left">
              <router-link class="link" :to="{ name: 'article', params: { articlePk: article.pk } }">
                {{ article.title }}  ({{ article.comment_count }})
              </router-link>
            </td>
            <td style="font-family: 'GmarketSansMedium';">{{ article.created_at | yyyyMMdd }}</td>
            <td style="font-family: 'GmarketSansMedium';">
              {{ article.like_count }}
            </td>
          </tr>
        </tbody>
      </table>
      <router-link :to="{ name: 'articleNew' }">
        <button style="float: right; font-family: 'GmarketSansMedium';" class="btn btn-outline-secondary waves-effect mb-4">게시글 작성</button>
      </router-link>
    </div>

  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleList',
  filters : {  
          // filter로 쓸 filter ID 지정
    yyyyMMdd : function(value){ 
            // 들어오는 value 값이 공백이면 그냥 공백으로 돌려줌
            if(value == '') return '';
        
            // 현재 Date 혹은 DateTime 데이터를 javaScript date 타입화
            var js_date = new Date(value);

            // 연도, 월, 일 추출
            var year = js_date.getFullYear();
            var month = js_date.getMonth() + 1;
            var day = js_date.getDate();

            // 월, 일의 경우 한자리 수 값이 있기 때문에 공백에 0 처리
            if(month < 10){
              month = '0' + month;
            }

            if(day < 10){
              day = '0' + day;
            }

            // 최종 포맷 (ex - '2021-10-08')
            return year + '-' + month + '-' + day;
    }
  },
  components: {
    NavBar
  },
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  },
}
</script>

<style scoped>
.link {
  color: #6441A5;
  text-decoration-line: none;
}

</style>