<template>
  <div class="nav">
    <el-menu
        router
        v-if="menu"
        :key="expend"
        :default-active="$route.path"
        mode="horizontal"
        :ellipsis="false"
        onselect=""
    >

      <div class="flex-grow"/>
      <el-menu-item route="/" index="/">主页</el-menu-item>
      <div class="disabled">
        <el-sub-menu index="3">
          <template #title>
            <el-avatar
                :size="40"
                :src="avatar"/>
          </template>
          <el-menu-item route="/user" index="3-1">个人中心</el-menu-item>
          <el-menu-item route="/user/works" index="3-2">创建作品</el-menu-item>
          <el-menu-item route="/" index="3-3" @click="logout">退出登录</el-menu-item>
          <el-menu-item route="/admin" index="3-4" v-if="is_admin">管理面板</el-menu-item>
        </el-sub-menu>
      </div>
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import {nextTick, ref, watch} from "vue";
import {logOutLogIn} from "@/router";
import {Expand, Fold} from "@element-plus/icons-vue";
import {user_info_md} from "@/services/modules/user";

let userData = user_info_md()
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
let is_expend = defineModel()
let menu = ref(true)
const logout = () => {
  logOutLogIn()
}
const expend = () => {
  is_expend.value = !is_expend.value
  menu.value = false
  nextTick(() => {
    menu.value = true
  })
}
</script>

<style>
.flex-grow {
  flex-grow: 1;
}

.nav {
  height: 100%;
  width: 100%;

  .el-menu {
    height: 100%;
    width: 100%;

    .el-sub-menu__title:hover,
    .el-menu-item:hover {
      background-color: rgba(242, 242, 242, 0) !important;
    }
  }

}

#user .el-icon {
  display: none;
}

.user-info {
  margin-top: 18px;
  display: flex;
  font-size: 18px;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

</style>
