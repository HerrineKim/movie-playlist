<template>
  <div 
  style="text-align:left; margin-left:40px; margin-top:60px; margin-right:60px;">
    <p
    style="font-family:MapoGoldenPier" :quote="quote"
    class="quote"
    >
      {{ quote[0].sentence }}
    </p>
    <p 
    style="font-family:MapoGoldenPier;"
    class="quoteMovie"
    >
      {{ quote[0].movie }}
    </p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: "RandomQuotes",
  data() {
    return {
      quote: null,
      quotes: [
        {
          sentence: '앞으로 힘든 시기가 올 수도 있겠지. 하지만 그건 네가 항상 주목하지 않았던 무언가를 깨닫게 해줄거야.',
          movie: '-Good Will Hunting(굿윌헌팅)-',
        },
        {
          sentence: '강한 힘에는 그만큼의 책임이 따른다.',
          movie: '-The Sound of Music(사운드 오브 뮤직)-',
        },
        {
          sentence: '갑자기 시간 여행이 쓸모 없는 것처럼 느껴진다. 왜냐하면 인생의 모든 사소한 것들이 기쁨을 주기 때문이다.',
          movie: '-About Time(어바웃타임)-',
        },
        {
          sentence: '그 누구도 아닌 자기 걸음을 걸어라. 나는 특이하다는 것을 믿어라. 모두가 가는 줄에 서있을 필요가 없다. 스스로의 걸음으로 자기길을 가라. 바보같은 사람들이 뭐라고 하든간에.',
          movie: '-죽은 시인의 사회-',
        },
        {
          sentence: '남들보다 우수하다고 해서 고귀한 것은 아니다. 과거의 나보다 우수한 것이 진정으로 고귀한 것이다.',
          movie: '-킹스맨-',
        },
        {
          sentence: '두려움은 당신을 포로로 묶어 놓지만, 희망은 당신을 자유롭게 한다',
          movie: '-쇼생크 탈출-',
        },
        {
          sentence: '길은 모두에게 열려있지만 모두가 그 길을 가질 수 있는 건 아니다',
          movie: '-인턴-',
        },
        {
          sentence: '소중한 순간이 오면 따지지 말고 누릴 것 우리에게 내일이 있으리란 보장은 없으니까',
          movie: '-창문넘어 도망친 100세 노인',
        },
        {
          sentence: '당신은 나에게, 너무나 완벽합니다. 그리고 제 마음이 아파도 당신을 사랑할거에요.',
          movie: '-러브 액츄얼리-',
        },
        {
          sentence: '살아 가면서 너무 늦거나, 너무 이른건 없단다. 꿈을 이루는데 시간 제한은 없단다.',
          movie: '-벤자민 버튼의 시간은 거꾸로 간다-',
        },
        {
          sentence: '가끔 라디오에서 좋은 노래가 나올 때가 있어. 노래를 듣고 나선 들은 것만으로 행복해지기도 해. 만약 평생동안 듣고 싶은 노래가 있다면, 넌 그런 노래일 거야',
          movie: '-유 콜 잇 러브-',
        },
        {
          sentence: '당신은 내가 더 좋은 사람이 되고 싶게 만들어요',
          movie: '-이보다 더 좋을 순 없다',
        },
        {
          sentence: '진짜 실패자는 지는게 두려워서 도전조차 안하는 사람이야',
          movie: '-리틀 미스 선샤인-',
        },
        {
          sentence: '누군가를 마음 속에서 지울 순 있지만 사랑은 잊혀지지 않아요',
          movie: '-이터널 선샤인-',
        },
        {
          sentence: '용서는 그냥 미움한테 방 한 칸만 내주면 되는 거래',
          movie: '-내 머리 속의 지우개-',
        },
        {
          sentence: '난 비록 죽으면 쉽게 잊혀질 평범한 사람이지만, 영혼을 바쳐 평생 한 여자를 사랑했으니, 내 인생은 성공한 인생입니다',
          movie: '-노트북-',
        },
        {
          sentence: '자기 혼자 빛나는 별은 없어 별은 다 빛을 받아서 반사하는 거야',
          movie: '-라디오 스타-',
        },
        {
          sentence: '행동하지 않고는 결과 또한 없습니다',
          movie: '-슈타펜버그-',
        },
        {
          sentence: '지난일에 대해서 새로운 눈물을 낭비하지 말아라',
          movie: '-신과 함께 - 죄와 벌-',
        },
        {
          sentence: '운명이란 말야 노력하는 사람한테 우연이라는 다리를 놓아주는거야',
          movie: '-엽기적인 그녀-',
        },
        {
          sentence: '길이 너무 실없이 끝나버린다고 허탈해할 필요는 없어. 방향만 바꾸면 여기가 또 출발이잖아',
          movie: '-가을로-',
        },
        {
          sentence: '음악가들은 은퇴하지 않는다는 말을 들은 적이 있어요. 그들은 그들 안에 음악이 없을 때 멈춰요. 저는 제 안에 아직 음악이 있다고 장담합니다',
          movie: '-인턴-',
        },
        {
          sentence: '인생은 해결해야 할 문제가 아니라 경험해야 할 여정입니다',
          movie: '-곰돌이 푸-',
        },
        {
          sentence: '눈을 감지 말고 똑바로 봐. 두려움의 실체는 생각과 다를 수 있어',
          movie: '-니모를 찾아서-',
        },
        {
          sentence: '익숙한 곳을 벗어나 봐. 그것에 대한 보상은 분명 가치가 있을 거야',
          movie: '-라푼젤-',
        },
        {
          sentence: '다른 사람이 결정하는 인생은 살고싶지 않아',
          movie: '-리틀 포레스트-',
        },
        {
          sentence: '삶이란 그런거죠 무엇인가 끊임없이 흘려보내는 것',
          movie: '-라이프 오브 파이-',
        }
      ]
    }
  },
  methods: {
    randomQuote () {
      this.quote = _.sampleSize(this.quotes, 1)
    }
  },
  created() {
    this.randomQuote()
  }
}
</script>

<style scoped>
@font-face {
    font-family: 'MapoGoldenPier';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoGoldenPierA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.quote {
  font-size:25px;
  word-break:keep-all;
}
.quoteMovie {
  font-size: 18px;
}
</style>