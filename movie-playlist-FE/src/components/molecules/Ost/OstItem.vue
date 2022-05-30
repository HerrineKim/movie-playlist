<template>
  <div>
    <iframe
    width="560" height="315"
    :src="src"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
    >
    </iframe>
    <div v-for="OstInfo in OstInfos" :key="OstInfo.ost">
      {{ OstInfo.ost }} {{ OstInfo.artist }} {{ OstInfo.movie }}
      <button @click="selectVideo(OstInfo)">비디오 나와랏</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "OstItem",
  data() {
    return {
      src: "https://www.youtube.com/embed/RBNVmMgt1Bg",
      OstInfos: [
        {
          ost: 'See You Again (폴 워커 추모 엔딩곡) (분노의 질주 : 더 세븐(Fast & Furious 7) OST)',
          artist: 'Charlie Puth(찰리 푸스)',
          movie: '분노의 질주 : 더 세븐(Fast & Furious 7)',
          url: '_ogDymI9BKM' 
        },
        {
          ost: 'Listen (From the Motion Picture "Dreamgirls")',
          artist: 'Beyoncé(비욘세)',
          movie: '드림걸즈',
          url: 'honPlOzVRCU'
        },
        {
          ost: "Lady Marmalade (With Lil' Kim, Mya And Pink)",
          artist: 'Christina Aguilera(크리스티나 아길레라)',
          movie: '물랑 루즈',
          url: 'RQa7SvVCdZk'
        },
        {
          ost: 'Let It Go (From "Frozen"/Soundtrack Version)',
          artist: 'Idina Menzel(이디나 멘젤)',
          movie: '겨울왕국',
          url: 'moSFlvxnbgk'
        },
        {
          ost: 'I Will Always Love You',
          artist: 'Whitney Houston(휘트니 휴스턴)',
          movie: '보디가드',
          url: '3JWTaaS7LdU'
        },
        {
          ost: 'My Heart Will Go On (Love Theme from "Titanic")',
          artist: 'Celine Dion(셀린 디온)',
          movie: '타이타닉',
          url: '3gK_2XdjOdY'
        },
        {
          ost: 'Shape Of My Heart',
          artist: 'Sting(스팅)',
          movie: '레옹',
          url: 'QK-Z1K67uaA'
        },
        {
          ost: 'Lost Stars',
          artist: 'Adam Levine(Maroon 5)',
          movie: '비긴 어게인',
          url: 'cL4uhaQ58Rk'
        },
        {
          ost: 'Lose Yourself (From "8 Mile" Soundtrack)',
          artist: 'Eminem(에미넴)',
          movie: '8마일',
          url: '_Yhyp-_hX2s'
        },
        {
          ost: 'Creep',
          artist: 'Radiohead(라디오헤드)',
          movie: '시클로',
          url: 'XFkzRNyygfk'
        },
        {
          ost: 'Falling Slowly (With Marketa Irglova)',
          artist: 'Glen Hansard(글렌 한사드)',
          movie: '원스',
          url: 'S2ANkkdhWVY'
        },
        {
          ost: "Singin' In The Rain",
          artist: 'Gene Kelly(진 켈리)',
          movie: '사랑은 비를 타고',
          url: 'D1ZYhVpdXbQ'
        },
        {
          ost: 'I Just Called To Say I Love You',
          artist: 'Stevie Wonder(스티비 원더)',
          movie: '우먼 인 레드',
          url: 'wyXNQiRCfRg'
        },
        {
          ost: 'Skyfall',
          artist: 'Adele(아델)',
          movie: '007 스카이폴',
          url: 'zKrZDGTWLRc'
        },
        {
          ost: 'I Dreamed A Dream (From "Les Misérables")',
          artist: 'Anne Hathaway(앤 헤서웨이)',
          movie: '레 미제라블',
          url: 'g0cDp07uYP0'
        },
        {
          ost: 'Way Back Into Love (duet with Haley Bennett)',
          artist: 'Hugh Grant(휴 그랜트)',
          movie: '그 여자 작사 그 남자 작곡',
          url: '0bwWy67MsOU'
        },
        {
          ost: 'Butterfly (Play 크리스티나, 이승열, 호란, 알렉스, 박기영, 웨일, 정순용, 미키, 혜원, 장은아)',
          artist: '러브홀릭스(Loveholics)',
          movie: '국가대표',
          url: 'fLk-dYXs_rM'
        },
        {
          ost: 'Maria',
          artist: '김아중',
          movie: '미녀는 괴로워',
          url: 'vSkXfrJtbAw'
        },
        {
          ost: 'I Believe (엽기적인 그녀 O.S.T)',
          artist: '신승훈',
          movie: '엽기적인 그녀',
          url: 'uU02KEA7fZo'
        },
        {
          ost: '희재',
          artist: '성시경',
          movie: '국화꽃 향기',
          url: 'aWXy974QLCk'
        },
        {
          ost: '말리꽃',
          artist: '이승철',
          movie: '비천무',
          url: '7CheO99RfdY'
        },
        {
          ost: '나의 왕자님 (My Prince)',
          artist: '박보영',
          movie: '늑대소년',
          url: 'VH3W8kmQbVs'
        },
        {
          ost: '너에게 난 나에게 넌',
          artist: '자전거 탄 풍경',
          movie: '클래식',
          url: '5ysdHjaeGGU'
        },
        {
          ost: '너무 아픈 사랑은 사랑이 아니었음을',
          artist: '김광석',
          movie: '클래식',
          url: 'BQLgM0dhRGg'
        },
        {
          ost: '아마도 그건',
          artist: '홍민정',
          movie: '과속스캔들',
          url: '-cl8RG-rw94'
        },
        {
          ost: '날 그만 잊어요 (Guitar ver.)',
          artist: '거미',
          movie: '내 머리 속의 지우개',
          url: 'rRUlG9farOQ'
        },
        {
          ost: '조선의 마음',
          artist: '천우희',
          movie: '해어화',
          url: 'bXa47Sielrk'
        },
        {
          ost: 'Merry Christmas Mr. Lawrence',
          artist: 'Ryuichi Sakamoto(류이치 사카모토/坂本龍一)',
          movie: '전장의 크리스마스',
          url: '1OZDaRhHHyM'
        },
        {
          ost: "Oogway's Legacy",
          artist: 'Hans Zimmer(한스 짐머)',
          movie: '쿵푸 팬더 3',
          url: '2YqUCGMYQ28'
        },
        {
          ost: "Deborah's Theme [Once Upon a Time in America] (From “Once Upon A Time In The West”)",
          artist: 'Sissel(시셀)',
          movie: '원스 어폰 어 타임 인 아메리카',
          url: 'ZuurydOcKYM'
        },
        {
          ost: 'The Last Waltz (미도테마)',
          artist: '심현정',
          movie: '올드보이',
          url: '_DxjFs_dsR8'
        },
        {
          ost: 'The Whole Nine Yards ("냉정과 열정사이 (冷靜と情熱のあいだ)" 로부터)',
          artist: 'Yoshimata Ryo(요시마타 료)',
          movie: '냉정과 열정 사이',
          url: 'f8ZlsB28TZ0'
        },
        {
          ost: 'First Step',
          artist: 'Hans Zimmer(한스 짐머)',
          movie: '인터스텔라',
          url: 'HV1CMDhemt0'
        },
        {
          ost: 'あの夏へ (어느 여름날) (센과 치히로의 행방불명 OST)',
          artist: 'Hinata Miyuki(히나타 미유키)',
          movie: '센과 치히로의 행방불명',
          url: 'iOYAl37AScY'
        },
        {
          ost: '공중 산책',
          artist: 'Hisaishi Joe(히사이시 조/久石 讓)',
          movie: '하울의 움직이는 성',
          url: '1cW82FMWvzU'
        },
        {
          ost: "Gabriel's Oboe",
          artist: 'Ennio Morricone(엔니오 모리꼬네)',
          movie: '미션',
          url: 'lArnKBTe82I',
        },
        {
          ost: 'Cries And Whispers (우진테마)',
          artist: '이지수',
          movie: '올드보이',
          url: 'vh2LWnenZvw'
        },
        {
          ost: "변하지 않는 것 (Strings ver.)",
          artist: 'Yoshida Kiyoshi(요시다 키요시)',
          movie: '시간을 달리는 소녀',
          url: 'Lq2-HHP04jM'
        },
        {
          ost: 'Come What May (With Ewan Mcgregor)',
          artist: 'Nicole Kidman(니콜 키드먼)', 
          movie: '물랑 루즈',
          url: 'ELkO5oB5r9M'
        },
        {
          ost: 'A Winter Story (러브레터 OST)',
          artist: 'Remedios(레메디오스)',
          movie: '러브레터',
          url: '4YlWxDD3-OE'
        },
        {
          ost: '인생의 회전목마',
          artist: 'Hisaishi Joe(히사이시 조/久石 讓)',
          movie: '하울의 움직이는 성',
          url: 'f7SS57LFPco'
        },
        {
          ost: 'Quizas Quizas Quizas',
          artist: 'Nat King Cole(냇 킹 콜)',
          movie: '화양연화',
          url: '_Fg95PhPg6s'
        },
        {
          ost: 'Happy Together',
          artist: 'Turtles(터틀즈)',
          movie: '춘광사설',
          url: '9ZEURntrQOg'
        },
        {
          ost: 'Cucurrucucu Paloma (Live 1995)',
          artist: 'Caetano Veloso(까에따누 벨로주)',
          movie: '그녀에게',
          url: 'huQGD0N42K4'
        },
        {
          ost: 'Piano Solo',
          artist: 'Ennio Morricone(엔니오 모리꼬네)',
          movie: '러브 어페어',
          url: 'AD_DJR1Vyx4'
        },
        {
          ost: "드뷔시: 아라베스크 1번",
          artist: 'Balázs Szokolay(발라스 쇼콜라이)',
          movie: '호로비츠를 위하여, 릴리 슈슈의 모든 것',
          url: 'jiKb-JzJFQM'
        },

        {
          ost: 'Romance',
          artist: 'Yuhki Kuramoto(유키 구라모토/倉本裕基)',
          movie: '달콤한 인생',
          url: '71EmgVktns4'
        },
        {
          ost: '돌이킬 수 없는 걸음',
          artist: '이병우',
          movie: '장화, 홍련',
          url: 'oeLHy3dIiXs' 
        },
        {
          ost: 'City of Stars',
          artist: 'Ryan Gosling & Emma Stone',
          movie: '라라랜드',
          url: 'GTWqwSNQCcg'
        },
        {
          ost: 'Speechless',
          artist: 'Naomi Scott',
          movie: '알라딘',
          url: 'mw5VIEIvuMI'
        },
        {
          ost: 'Love Me Like You Do',
          artist: 'Ellie Goulding',
          movie: '그레이의 50가지 그림자',
          url: 'RuxfYnDl6p0'
        },
        {
          ost: 'Hakuna Matata',
          artist: 'Billy Eichner & Seth Rogen & JD McCrary & Donald Glover',
          movie: '라이온 킹',
          url: 'yUioIn8rPPM'
        },
        {
          ost: 'How Long Will I Love You',
          artist: 'Ellie Goulding',
          movie: '어바웃 타임',
          url: 'qhanxrVLepQ'
        }
      ] 
    }
  },
  methods: {
    selectVideo(OstInfo) {
      this.src = `https://www.youtube.com/embed/${OstInfo.url}`
    }
  }
}
</script>

<style>
</style>