<template>
  <div class="sidebar">
    <a-menu
      style="height: 100%; overflow-y: scroll"
      :default-selected-keys="['1']"
      :default-open-keys="['sub1']"
      mode="inline"
      theme="dark"
      :inline-collapsed="collapsed"
    >
      <!-- <router-link to="/writedown"> -->
        <a-menu-item key="1">
          <span className="anticon"
            ><i class="icon iconfont icon-CurrencyConverter"
          /></span>
          <span><span> Download Write down</span></span>
        </a-menu-item>
        <!-- </router-link
      > -->
      <a-menu-item key="2">
        <router-link to="/writedown"><span className="anticon"
          ><i class="icon iconfont icon-CurrencyConverter"
        /></span>
        <span>Download Write down</span></router-link
      >
      </a-menu-item>
      <a-menu-item key="3">
        <span className="anticon"
          ><i class="icon iconfont icon-CurrencyConverter"
        /></span>
        <span>Option 3</span>
      </a-menu-item>
      <a-sub-menu key="sub1">
        <template v-slot:title
          ><span className="anticon"
            ><i class="icon iconfont icon-CurrencyConverter" /></span
          ><span>Navigation One</span></template
        >
        <a-menu-item key="5"> Option 5 </a-menu-item>
        <a-menu-item key="6"> Option 6 </a-menu-item>
        <a-menu-item key="7"> Option 7 </a-menu-item>
        <a-menu-item key="8"> Option 8 </a-menu-item>
      </a-sub-menu>
      <a-sub-menu key="sub2">
        <template v-slot:title
          ><span className="anticon"
            ><i class="icon iconfont icon-CurrencyConverter" /></span
          ><span>Navigation Two</span></template
        >
        <a-menu-item key="9"> Option 9 </a-menu-item>
        <a-menu-item key="10"> Option 10 </a-menu-item>
        <a-sub-menu key="sub3" title="Submenu">
          <a-menu-item key="11"> Option 11 </a-menu-item>
          <a-menu-item key="12"> Option 12 </a-menu-item>
        </a-sub-menu>
      </a-sub-menu>
    </a-menu>
  </div>
</template>

<script>
import bus from "../eventBus";
export default {
  name: "Sidebar",
  data() {
    return {
      collapsed: false,
    };
  },
  created() {
    bus.$on("SidebarChanged", (message) => {
      this.collapsed = !this.collapsed;
      console.log(message);
    });
  },
};
</script>

<style scoped>
.sidebar {
  width: 20%;
  height: 100%;
  margin-left: -8px;
  position: fixed;
}

::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: #2c3e50;
}

::-webkit-scrollbar-thumb {
  background: #253443;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #253443;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:active {
  background: #253443;
  border-radius: 10px;
}
</style>