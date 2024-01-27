<template>
  <el-menu
      router :default-active="$route.path"
      class="aside-menu"
      :collapse="is_expend"
  >
    <div class="logo">
      <h2 v-if="!is_expend">YuDream</h2>
    </div>
    <el-divider/>
    <div class="user-info">
      <el-avatar :src="avatar"/>
      <div v-if="!is_expend">Hi {{ nickname }}!</div>
      <div v-if="is_expend">Hi</div>
    </div>
    <el-divider/>
    <div class="function">
      <div v-if="!is_expend" class="aside-title">
        用户中心
      </div>
      <el-menu-item route="/user" index="/user">
        <el-icon>
          <home-filled/>
        </el-icon>
        <span slot="title" v-if="!is_expend">仪表盘</span>
      </el-menu-item>
      <el-menu-item route="/user/creation" index="/user/creation">
        <el-icon>
          <Monitor/>
        </el-icon>
        <span v-if="!is_expend" slot="title">创作中心</span>
      </el-menu-item>
      <el-menu-item route="/user/works" index="/user/works">
        <el-icon>
          <Notebook/>
        </el-icon>
        <span v-if="!is_expend" slot="title">我的作品</span>
      </el-menu-item>
      <el-menu-item route="/user/collection" index="/user/collection">
        <el-icon>
          <Star/>
        </el-icon>
        <span v-if="!is_expend" slot="title">我的收藏</span>
      </el-menu-item>
      <el-menu-item route="/user/setting" index="/user/setting">
        <el-icon>
          <Setting/>
        </el-icon>
        <span v-if="!is_expend" slot="title">资料修改</span>
      </el-menu-item>
      <div class="admin" v-if="is_admin">
        <div v-if="!is_expend" class="aside-title">
          管理
        </div>

        <el-menu-item route="/admin" index="/admin">
          <el-icon>
            <Grid/>
          </el-icon>
          <span v-if="!is_expend" slot="title">管理中心</span>
        </el-menu-item>
      </div>
    </div>
  </el-menu>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {
  DataLine, Grid,
  HomeFilled,
  Menu as IconMenu, Monitor, Notebook, Setting, Star, User,
} from '@element-plus/icons-vue'
import {user_info_md} from "@/services/modules/user";

const is_expend = defineModel()
const userData = user_info_md()
let nickname = ref("")
let avatar = ref("")
let is_admin = ref(false)
userData.then((res) => {
  nickname.value = res?.['nickname']
  avatar.value = res?.['avatar']
  if (res?.['role'] >= 3) {
    is_admin.value = true
  }
})
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

.aside-menu {
  position: fixed;
  width: 200px;
  min-height: Calc(100vh - 60px);

  .el-divider {
    margin: 0 0;
  }
}

.function {
  .el-menu-item {
    margin: 5px;
    height: 40px;
    border-radius: 5px;
    color: rgb(52, 58, 64);
  }

  .el-menu-item:hover {
    color: black;
    background-color: rgb(229, 229, 229) !important;
  }

  .el-menu-item.is-active {
    color: white;
    background-color: rgb(32, 201, 151) !important;
  }
}

.logo {
  height: 50px;
  font-size: 15px;
  font-family: font1, serif;
  padding-top: 10px;
  margin-bottom: 10px;
}

.user-info {
  margin: 5px 0 5px 0;
}

.aside-title {
  font-size: 12px;
  margin-top: 20px;
  padding-left: 10px;
  text-align: left;
  width: 100%;
}

.el-menu--collapse {
  width: 40px;

  .el-menu-item {
    margin: 5px 0 5px 0;
    height: 40px;
    border-radius: 5px;
    color: rgb(52, 58, 64);
  }

  .el-menu-item:hover {
    color: black;
    background-color: rgb(229, 229, 229) !important;
  }

  .el-menu-item.is-active {
    color: white;
    background-color: rgb(32, 201, 151) !important;
  }

  .el-menu-item__title {
    display: none;
  }

  .el-menu-item__icon {
    margin: 0 0 0 0;
  }

  .el-menu-item__index {
    display: none;
  }

  .el-menu-item__content {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .el-menu-item__content:hover {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content.is-active {

    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content.is-active:hover {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content:hover {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content.is-active {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content.is-active:hover {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content:hover {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content.is-active {
    background-color: rgba(242, 242, 242, 0) !important;
  }

  .el-menu-item__content.is-active:hover {
    background-color: rgba(242, 242, 242, 0) !important;
  }
}

</style>
