<template>
  <div id="app">
    <nav-bar></nav-bar>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/templates/NavBar.vue'

export default {
  name: 'App',
  components: { NavBar },
  data() {
    return {
      Ost: [
        'See You Again (폴 워커 추모 엔딩곡) (분노의 질주 : 더 세븐(Fast & Furious 7) OST)',
        'Listen (From the Motion Picture "Dreamgirls")',
        "Lady Marmalade (With Lil' Kim, Mya And Pink)",
        'Let It Go (From "Frozen"/Soundtrack Version)',
        'I Will Always Love You',
        'My Heart Will Go On (Love Theme from "Titanic")',
        'Shape Of My Heart',
        'Lost Stars',
        'Lose Yourself (From "8 Mile" Soundtrack)',
        'Creep',
        'Falling Slowly (With Marketa Irglova)',
        "Singin' In The Rain",
        'I Just Called To Say I Love You',
        'Skyfall',
        'I Dreamed A Dream (From "Les Misérables")',
        'Way Back Into Love (duet with Haley Bennett)',
        'Butterfly (Play 크리스티나, 이승열, 호란, 알렉스, 박기영, 웨일, 정순용, 미키, 혜원, 장은아)',
        'Maria',
        'I Believe (엽기적인 그녀 O.S.T)',
        '희재',
        '말리꽃',
        '나의 왕자님 (My Prince)',
        '너에게 난 나에게 넌',
        '너무 아픈 사랑은 사랑이 아니었음을',
        '아마도 그건',
        '날 그만 잊어요 (Guitar ver.)',
        '조선의 마음',
        'Merry Christmas Mr. Lawrence',
        "Oogway's Legacy",
        "Deborah's Theme [Once Upon a Time in America] (From “Once Upon A Time In The West”)",
        'The Last Waltz (미도테마)',
        'The Whole Nine Yards ("냉정과 열정사이 (冷靜と情熱のあいだ)" 로부터)',
        'First Step',
        'あの夏へ - Ano Natsue (어느 여름날) (센과 치히로의 행방불명 OST)',
        '공중 산책',
        "Gabriel's Oboe",
        'Cries And Whispers (우진테마)',
        "삽입곡 '변하지 않는 것' (Strings ver.)",
        'Come What May (With Ewan Mcgregor)',
        'A Winter Story (러브레터 OST)',
        '인생의 회전목마 (하울의 움직이는 성)',
        'Quizas Quizas Quizas',
        'Happy Together',
        'Cucurrucucu Paloma (Live 1995)',
        'Piano Solo',
        "드뷔시: 아라베스크 1번 (영화 '호로비츠를 위하여', '릴리 슈슈의 모든것')",
        'Romance',
        '돌이킬 수 없는 걸음 (장화, 홍련)',
        'City of Stars',
        'Speechless',
        'Love Me Like You Do',
        'Hakuna Matata',
        'How Long Will I Love You',
        ],
      Artist: [
        'Charlie Puth(찰리 푸스)',
        'Beyoncé(비욘세)',
        'Christina Aguilera(크리스티나 아길레라)',
        'Idina Menzel(이디나 멘젤)',
        'Whitney Houston(휘트니 휴스턴)',
        'Celine Dion(셀린 디온)',
        'Sting(스팅)',
        'Adam Levine(Maroon 5)',
        'Eminem(에미넴)',
        'Radiohead(라디오헤드)',
        'Glen Hansard(글렌 한사드)',
        'Gene Kelly(진 켈리)',
        'Stevie Wonder(스티비 원더)',
        'Adele(아델)',
        'Anne Hathaway(앤 헤서웨이)',
        'Hugh Grant(휴 그랜트)',
        '러브홀릭스(Loveholics)',
        '김아중',
        '신승훈',
        '성시경',
        '이승철',
        '박보영',
        '자전거 탄 풍경',
        '김광석',
        '홍민정',
        '거미',
        '천우희',
        'Ryuichi Sakamoto(류이치 사카모토/坂本龍一)',
        'Hans Zimmer(한스 짐머)',
        'Sissel(시셀)',
        '심현정',
        'Yoshimata Ryo(요시마타 료)',
        'Hans Zimmer(한스 짐머)',
        'Hinata Miyuki(히나타 미유키)',
        'Hisaishi Joe(히사이시 조/久石 讓)',
        'Ennio Morricone(엔니오 모리꼬네)',
        '이지수',
        'Yoshida Kiyoshi(요시다 키요시)',
        'Nicole Kidman(니콜 키드먼)', 
        'Ttoyo Studio Orchestra',
        'Elizabeth Bright(엘리자베스 브라이트)',
        'Nat King Cole(냇 킹 콜)',
        'Turtles(터틀즈)',
        'Caetano Veloso(까에따누 벨로주)',
        'Ennio Morricone(엔니오 모리꼬네)',
        'Balázs Szokolay(발라스 쇼콜라이)',
        'Yuhki Kuramoto(유키 구라모토/倉本裕基)',
        '이병우',
        'Ryan Gosling & Emma Stone',
        'Naomi Scott',
        'Ellie Goulding',
        'Billy Eichner & Seth Rogen & JD McCrary & Donald Glover',
        'Ellie Goulding',
        ],
      OstUrls: [
        'https://youtu.be/_ogDymI9BKM', // See you~
        'https://youtu.be/honPlOzVRCU', // Listen
        'https://youtu.be/RQa7SvVCdZk', // Lady Marmalad
        'https://youtu.be/moSFlvxnbgk', // Let it go
        'https://youtu.be/3JWTaaS7LdU', // I will always
        'https://youtu.be/3gK_2XdjOdY', // My Heart will go on
        'https://youtu.be/QK-Z1K67uaA', // shape of my heard
        'https://youtu.be/cL4uhaQ58Rk', // Lost Stars
        'https://youtu.be/_Yhyp-_hX2s', // Lose Yourself
        'https://youtu.be/XFkzRNyygfk', // Creep
        'https://youtu.be/S2ANkkdhWVY', // Falling~
        'https://youtu.be/D1ZYhVpdXbQ', // Singin'~
        'https://youtu.be/wyXNQiRCfRg', // I Just~
        'https://youtu.be/zKrZDGTWLRc', // Skyfall
        'https://youtu.be/g0cDp07uYP0', // I dreamed~
        'https://youtu.be/0bwWy67MsOU', // Way Back Into~
        'https://youtu.be/fLk-dYXs_rM', // Butterfly
        'https://youtu.be/vSkXfrJtbAw', // Maria
        'https://youtu.be/uU02KEA7fZo', // I believe
        'https://youtu.be/aWXy974QLCk', // 희재
        'https://youtu.be/7CheO99RfdY', // 말리꽃
        'https://youtu.be/VH3W8kmQbVs', // 나의 왕자님
        'https://youtu.be/5ysdHjaeGGU', // 너에게 난 나에게 넌
        'https://youtu.be/BQLgM0dhRGg', // 너무 아픈 사랑은~
        'https://youtu.be/-cl8RG-rw94', // 아마도 그건
        'https://youtu.be/rRUlG9farOQ', // 날 그만~
        'https://youtu.be/bXa47Sielrk', // 조선의 마음
        'https://youtu.be/1OZDaRhHHyM', // Merry Christmas~
        'https://youtu.be/2YqUCGMYQ28', // Oogway~
        'https://youtu.be/ZuurydOcKYM', // Deborah~
        'https://youtu.be/_DxjFs_dsR8', // The Last Waltz
        'https://youtu.be/f8ZlsB28TZ0', // The Whole Nine Yards
        'https://youtu.be/HV1CMDhemt0', // First Step
        'https://youtu.be/iOYAl37AScY', // 어느 여름날
        'https://youtu.be/1cW82FMWvzU', // 공중 산책
        'https://youtu.be/lArnKBTe82I', // Gabriel's Oboe
        'https://youtu.be/vh2LWnenZvw', // Cries And Whispers
        'https://youtu.be/Lq2-HHP04jM', // 변하지 않는 것
        'https://youtu.be/ELkO5oB5r9M', // Come What May
        'https://youtu.be/4YlWxDD3-OE', // A Winter Story
        'https://youtu.be/f7SS57LFPco', // 인생의 회전목마
        'https://youtu.be/_Fg95PhPg6s', // Quizas Quizas Quizas
        'https://youtu.be/9ZEURntrQOg', // Happy Together
        'https://youtu.be/huQGD0N42K4', // Cucurrucucu~
        'https://youtu.be/AD_DJR1Vyx4', // Piano Solo
        'https://youtu.be/jiKb-JzJFQM', // 드뷔시~
        'https://youtu.be/71EmgVktns4', // Romance
        'https://youtu.be/oeLHy3dIiXs', // 돌이킬 수 없는 걸음
        'https://youtu.be/GTWqwSNQCcg', // City of Stars
        'https://youtu.be/mw5VIEIvuMI', // Speechless
        'https://youtu.be/RuxfYnDl6p0', // Love Me Like You Do
        'https://youtu.be/yUioIn8rPPM', // Hakuna Matata
        'https://youtu.be/qhanxrVLepQ', // How Long~ 
      ],
    }
  },
  methods: {
    fetchCurrentUser () {
      this.$store.dispatch('fetchCurrentUser')
    },
    fetchBoxoffice () {
      this.$store.dispatch('fetchBoxoffice')
    },
  },
  created () {
    this.fetchBoxoffice()
    this.fetchCurrentUser()
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
