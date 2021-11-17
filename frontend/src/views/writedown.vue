<template>
  <div style="height: 100%">
    <Header @changeHome="changewidth" />
    <Sidebar />
    <div :class="collapsed ? 'mainBlock-collapsed' : 'mainBlock'">
      <div class="datePickerZone">
        <div style="padding: 50px; font-size: 30px; color: #0082c3">
          Please choose the date range
        </div>
        <br />
      <div>
        <a-range-picker v-model="date" v-on:change="sth = $event.target.date" :format="dateFormat" /></div>
        <br />
        <button class="download-button" @click="Download(sth)">
          Download CSV File
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Sidebar from "@/components/Sidebar.vue";
// import axios from "axios";
export default {
  name: "WriteDown",
  components: { Header, Sidebar },
  data() {
    return {
      dateFormat: "DD/MM/YYYY",
      date: null,
    };
  },
  methods: {
    // onChange(date, dateString) {
    //   console.log(dateString);
    // },
    Download(sth) {
      console.log(sth);
    //   let data = {
    //     startTime: this.time3[0],
    //     endTime: this.time3[1],
    //   };
    //   axios
    //     .post(`http://127.0.0.1:8000/writedown/`, data)
    //     .then((response) => console.log(response.data));
    // },
  },
  },
};
</script>

<style>
.datePickerZone{
    text-align: center;
}

.download-button {
  overflow: hidden;
  border: none;
  font-family: inherit;
  font-size: 15px;
  color: #fff;
  background: #2c3e50;
  cursor: pointer;
  margin-top: 20px;
  width: 20%;
  padding: 1%;
  display: inline-block;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: 500;
  outline: none;
  position: relative;
  transition: all 0.3s;
  margin-top: 50px;
}

.download-button:hover {
  background: rgba(0,130,195,1)
}

.download-button:active {
  background: rgba(135, 172, 214, 1);
  top: 2px;
}

.download-button:after {
  width: 30%;
  height: 200%;
  background: rgba(255, 255, 255, 0.1);
  z-index: 1;
  right: 0;
  top: 0;
  margin: -5px 0 0 -5px;
  -webkit-transform-origin: 0 0;
  -webkit-transform: rotate(-20deg);
  -moz-transform-origin: 0 0;
  -moz-transform: rotate(-20deg);
  -ms-transform-origin: 0 0;
  -ms-transform: rotate(-20deg);
  transform-origin: 0 0;
  transform: rotate(-20deg);
  content: "";
  position: absolute;
  transition: all 0.3s;
}

.download-button:hover:after {
  width: 40%;
}

.download-button:hover:before {
  font-size: 150%;
}
</style>