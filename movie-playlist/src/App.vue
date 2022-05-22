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
        '하얀나비',
        '너무 아픈 사랑은 사랑이 아니었음을',
        '아마도 그건',
        '나 항상 그대를',
        '이차선 다리',
        '날 그만 잊어요 (Guitar ver.)',
        '조선의 마음',
        '인연 (동녘바람)',
        'Merry Christmas Mr. Lawrence',
        "Oogway's Legacy",
        "Deborah's Theme [Once Upon a Time in America] (From “Once Upon A Time In The West”)",
        'The Last Waltz (미도테마)',
        'The Whole Nine Yards ("냉정과 열정사이 (冷靜と情熱のあいだ)" 로부터)',
        'First Step',
        'あの夏へ - Ano Natsue (어느 여름날) (센과 치히로의 행방불명 OST)',
        '공중 산책',
        "Gabriel's Oboe",
        '에필로그 (Epilogue)',
        'Cries And Whispers (우진테마)',
        "삽입곡 '변하지 않는 것' (Strings ver.)",
        '684부대',
        '만추(晩秋)',
        'Come What May (With Ewan Mcgregor)',
        '어느 여름날 (あの夏へ)',
        'A Winter Story (러브레터 OST)',
        '인생의 회전목마 (하울의 움직이는 성)',
        'Quizas Quizas Quizas',
        'Happy Together',
        'Cucurrucucu Paloma (Live 1995)',
        'Piano Solo',
        "드뷔시: 아라베스크 1번 (영화 '호로비츠를 위하여', '릴리 슈슈의 모든것')",
        "Poverty/Deborah's Theme (Once Upon A Time In America)",
        'Romance',
        '돌이킬 수 없는 걸음 (장화, 홍련)'
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
        '심은경',
        '김광석',
        '홍민정',
        '이선희',
        '차태현',
        '거미',
        '천우희',
        '이선희',
        'Ryuichi Sakamoto(류이치 사카모토/坂本龍一)',
        'Hans Zimmer(한스 짐머)',
        'Sissel(시셀)',
        '심현정',
        'Yoshimata Ryo(요시마타 료)',
        'Hans Zimmer(한스 짐머)',
        'Hinata Miyuki(히나타 미유키)',
        'Hisaishi Joe(히사이시 조/久石 讓)',
        'Ennio Morricone(엔니오 모리꼬네)',
        '이동준',
        '이지수',
        'Yoshida Kiyoshi(요시다 키요시)',
        '조영욱',
        '탕웨이(TANG Wei)',
        'Nicole Kidman(니콜 키드먼)', 
        'Hisaishi Joe(히사이시 조/久石 讓)',
        'Ttoyo Studio Orchestra',
        'Elizabeth Bright(엘리자베스 브라이트)',
        'Nat King Cole(냇 킹 콜)',
        'Turtles(터틀즈)',
        'Caetano Veloso(까에따누 벨로주)',
        'Ennio Morricone(엔니오 모리꼬네)',
        'Balázs Szokolay(발라스 쇼콜라이)',
        'Die 12 Cellisten Der Berliner Philharmoniker(베를린 필 12 첼리스트)',
        'Yuhki Kuramoto(유키 구라모토/倉本裕基)',
        '이병우'
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
