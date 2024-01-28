<template>
  <el-menu
      router :default-active="$route.path"
      class="aside-menu"
  >
    <div class="logo">
      <h2>YuDream</h2>
    </div>
    <el-divider/>
    <div class="user-info">
      <el-avatar :src="avatar"/>
      <div>Hi {{ nickname }}!</div>
    </div>
    <el-divider/>
    <div class="function">
      <div class="aside-title">
        管理中心
      </div>
      <el-menu-item route="/admin" index="/admin">
        <el-icon>
          <home-filled/>
        </el-icon>
        <span slot="title">仪表盘</span>
      </el-menu-item>
      <el-menu-item route="/admin/users" index="/admin/users">
        <el-icon>
          <User/>
        </el-icon>
        <span slot="title">用户管理</span>
      </el-menu-item>
      <el-menu-item route="/admin/works" index="/admin/works">
        <el-icon>
          <Notebook/>
        </el-icon>
        <span slot="title">作品管理</span>
      </el-menu-item>
      <el-menu-item route="/admin/model" index="/admin/model">
        <el-icon>
          <Monitor/>
        </el-icon>
        <span slot="title">模型信息</span>
      </el-menu-item>
      <div class="admin">
        <div class="aside-title">
          系统设置
        </div>
        <el-menu-item route="/admin/setting" index="/admin/setting">
          <el-icon>
            <Setting/>
          </el-icon>
          <span slot="title">系统选项</span>
        </el-menu-item>
      </div>
      <div>
        <div class="aside-title">
          个人中心
        </div>
        <el-menu-item route="/user" index="/user">
          <el-icon>
            <Menu/>
          </el-icon>
          <span slot="title">用户面板</span>
        </el-menu-item>
      </div>
    </div>
  </el-menu>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {
  Grid,
  HomeFilled,
  Monitor, Notebook, Setting, User,
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
