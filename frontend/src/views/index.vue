<template>
  <div style="height: 100%">
    <Header @changeHome="changewidth" />
    <Sidebar />
    <div :class="collapsed ? 'mainBlock-collapsed' : 'mainBlock'">
      <div id="myChart" style="height: 40%"></div>

    </div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Sidebar from "@/components/Sidebar.vue";

export default {
  name: "Home",
  components: {
    Header,
    Sidebar,
  },

  data() {
    return {
      collapsed: false,
    };
  },
  mounted() {
    //this.$root => app
    let myChart1 = this.$echarts.init(
      document.getElementById("myChart"),
      null,
      {
        width: 450,
        height: 350,
      }
    );
    // 绘制图表
    myChart1.setOption({
      title: { text: "总用户量" },
      tooltip: {},
      xAxis: {
        data: ["12-3", "12-4", "12-5", "12-6", "12-7", "12-8"],
      },
      yAxis: {},
      series: [
        {
          name: "用户量",
          type: "line",
          data: [5, 20, 36, 10, 10, 20],
        },
      ],
    });
  },
  methods: {
    changewidth(message) {
      this.collapsed = !this.collapsed;
      console.log(message);
    },
  },
};
</script>

<style>
.mainBlock {
  width: 75%;
  left: 22%;
  position: absolute;
  background: #fff;
  display: block;
  height: 80%;
  top: 80px;
  box-shadow: 2px 2px 5px rgb(0 0 0 / 7%);
  transition: all 0.2s;
}

.mainBlock-collapsed {
  width: 85%;
  left: 10%;
  position: absolute;
  background: #fff;
  display: block;
  height: 80%;
  top: 80px;
  box-shadow: 2px 2px 5px rgb(0 0 0 / 7%);
  transition: all 0.2s;
}
</style>