<template>
  <div class="header-navbar">
    <div class="container">
      <router-link to="/" class="logo navbar-brand"
        >Finance & Solution
      </router-link>
      <div class="nav-no-collapse navbar-left">
        <a-button @click="changeSidebar">
          <i
            :class="
              collapsed
                ? 'icon iconfont icon-zhankai'
                : 'icon iconfont icon-shouqi'
            "
          ></i>
        </a-button>
      </div>
      <div class="nav navbar-nav pull-right">
        <a-menu mode="horizontal">
          <a-menu-item key="mail"> GROUP </a-menu-item>
          <a-sub-menu>
            <template v-slot:title class="submenu-title-wrapper">
              Useful Links</template
            >
            <a-menu-item-group>
              <a-menu-item key="setting:1">
                <a href="" target="_blank">
                  <img
                    src="https://blgfilespr.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/658/2020/02/06174224/google-search.png"
                    class="wpmm-custom-image"
                    style="width: 30px; margin: 5px"
                  />DECATSearch</a
                >
              </a-menu-item>
              <a-menu-item key="setting:2"
                ><a
                  href="https://identity-access.decathlon.net/identityiq/home.jsf"
                  target="_blank"
                >
                  <img
                    src="https://blgfilespr.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/658/2020/02/10095703/my-identity-access-1.png"
                    class="wpmm-custom-image"
                    style="width: 30px; margin: 5px"
                  />Identity Ac.</a
                >
              </a-menu-item>
              <a-menu-item key="setting:3"
                ><a
                  href="https://eone92.subsidia.org/jde/E1Menu.maf"
                  target="_blank"
                  alt="Eone"
                  rel="noopener noreferrer"
                >
                  <img
                    src="https://blgfilespr.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/658/2020/03/11160011/finance-eone.png"
                    class="wpmm-custom-image"
                    style="width: 30px; margin: 5px"
                  />
                  Eone</a
                >
              </a-menu-item>
              <a-menu-item key="setting:4"
                ><a
                  href="https://support.decathlon.net/idm-service/idm/v0/login?tenant=380531272_db&token=4p%2FWoeZDBwudU0hwhEFVAROM9S0bk6MybS86zib%2Fm8iGYjdOMbXpQh67fFCtHcxbHVvyj%2FVQ564m%2B3ke5n7O8cpp8i%2BFhUGFgsVZ%2F3lEqFejeJwTIZB3gk%2FWASE2Ju%2FSDIVFOzahXGE7Al%2FwfzXEjwMqYCQCQC9GaPAyw1Tcns9dgPzjGuuvC7vKavsgYaLwFdsvn8iy1wy7G4fm9sdnu9O9bFlUETgY1u7Pn6iR%2F%2B33WmLKc10LGtKYNbXkOCTtmbIMHCI8lUUFYkJnwCTkb4SVBaldW7u41eNCixG9o8WQPh0hB1tCatOtgpXR3f%2BIiLZ88xXq3nTOmEt%2FJs0OrWDXht%2BcBm6fKZKlueIWOTomEzgRLVN0QX0%2B7oW2IBX42os1mksMEZ2dqZNdTjD0n9abhcMV%2BOFHPLf0Uv3RvcVoQ0Gsu7ZCO%2BioXrTmBjdK%2BorNOK9reCeJmOgQj7GQFQ4xnmvIw4vybZPZq5RVgslscPcSJdeyBU87HWr9kPhgKuuCXgZdTZB9ZqcZyUqwJJputdIJE%2BAxJI3YqVwjbdUhVsdpDLsYYtLbdf9xpQnN1FbSMQrdngZkFafZ2XGAwFgGy%2Fr9NOtW4pDu2wH%2BhY7Lutc4CwL%2BlRxkrIfl3%2BtZ9rMm2WStg0larDxVqHufEerWrrABh9CIAWZpUnXpoMk1pSLxviFPliN7qsUOiH6riRRK7F72VCYH4K3VaBjsIL3mJqFjEl6p9CCrClycLFHKZ8jDpl5rcA7nkNhXwOpatZ3Ps8Nykv4RcKQbmdN17gtgU9lDvSFi%2FP0%2F%2BLfInpHkLOtWpDEhZBwGg6E4uTHdcfEiKCktzx34tgcMnj59UlESWcSanb8MaJNql2543z88kPNmcqanJ%2F7q9b0ZxK%2F8DNOKJWHppN5AqKA89lLx9FQunvmF74Bx2cz7kC6dX9ll%2BX4sVKufUpRil%2BRjPKftb8cfm04V0UmlSHDw0AWka7qQQcaThsPeTX84XiIoTmhvo1xxQTVvjf0dDk9nFj1Cp213WIL%2Fl59lY%2F9LM9d9sT0UWMe24F5fXlm69OnpufyE320prlGfd%2BLCzJr1vnPg%2FAsZj5iXJd6LM3TYfOkz%2FRHZ68dhdX0bblUdsq8WfhfsTy%2B6L%2F5Grv5%2BjZkDvxN%2Fve%2BxhumNXMNroXHGd4qk1ETEVRWL8XjFP0d%2FBEq4J1sWoFjiuE1agbkSheTwQRmPF9vMo9QLQjOJ5HscuIAp3KyK1JA6FCukYbD%2FV9pM4nyv%2Fvl8m5Zz6S8cK011PcX9APD78KLa0SO7RgjkdoIEuCaU6fhmGjbycA4eWw%3D%3D&tryLocal=true"
                  target="_blank"
                >
                  <img
                    src="https://blgfilespr.s3.eu-west-1.amazonaws.com/wp-content/uploads/sites/658/2020/02/10110327/heldesk.png"
                    class="wpmm-custom-image"
                    style="width: 30px; margin: 5px"
                  />Helpdesk</a
                >
              </a-menu-item>
            </a-menu-item-group>
            <a-menu-item-group title="Item 2">
              <a-menu-item key="setting:3"> Option 3 </a-menu-item>
              <a-menu-item key="setting:4"> Option 4 </a-menu-item>
            </a-menu-item-group>
          </a-sub-menu>
          <a-menu-item key="alipay">
            <a
              href="https://antdv.com"
              target="_blank"
              rel="noopener noreferrer"
              >Navigation Four - Link</a
            >
          </a-menu-item>
        </a-menu>
      </div>
    </div>
  </div>
</template>


<script>
import bus from "../eventBus";
export default {
  name: "Header",
  data() {
    return {
      collapsed: false,
    };
  },
  methods: {
    changeSidebar() {
      bus.$emit("SidebarChanged", "change");
      this.collapsed = !this.collapsed;
      this.$emit('changeHome', "change")
    },
  },
};
</script>

<style scoped>
@import "../assets/style/public.css";
.nav {
  list-style: none;
}
.header-navbar {
  background-color: #fff;
  border: 0 none;
  border-radius: 0;
  background-clip: padding-box;
  margin: 0;
  min-height: 40px;
  color: #262626;
  box-shadow: 0px 1px 3px 0 rgb(0 0 0 / 10%);
  position: fixed;
  z-index: 99;
  width: 100%;
  height: 60px;
}

.pull-right {
  float: right;
  margin-right: 30px;
  width: 50%;
  height: 100%;
  padding: 10px;
}

.container {
  margin: 0;
  max-width: 1920px;
  width: 100%;
  height: 100%;
}

.logo {
  font-family: "Marcsc";
  color: #fff;
  font-size: 25px;
  display: inline-block;
  text-decoration: none;
  margin-left: 10px;
  height: 100%;
}

.navbar-brand {
  background: #34495e;
  color: #fff;
  font-weight: 700;
  width: 20%;
  margin-left: -8px;
  padding: 10px 15px;
  text-align: center;
  border-bottom: 1px solid #34495e;
}

.navbar-left {
  display: inline-flex;
  top: 0;
  position: absolute;
  height: 100%;
}

.navbar-left:hover {
  background-color: #0082c3;
}

.ant-btn:hover,
.ant-btn:focus {
  color: #fff;
  background-color: #0082c3;
}
</style>
