<script setup lang="ts">
import {Search} from "@element-plus/icons-vue";
import {ref} from "vue";
import {ElNotification} from "element-plus";
import {add_user_by_admin} from "@/services/modules/user";

let role = ref('')
const handleAddUser = () => {
  addDrawer.value = true
}
let user = defineModel()
let username = ref('')
let addDrawer = ref(false)
let addUserInfo = ref({
  'username': '',
  'nickname': '',
  'password': '',
  'email': '',
  'phone': '',
  'role': ''
})
const handleSearch = () => {
  user.value = username.value
}
async function add_user() {
  if (addUserInfo.value['username'] === "") {
    ElNotification({
      title: "用户名不能为空",
      type: "error"
    })
  }
  else if (addUserInfo.value['password'] === "") {
    ElNotification({
      title: "密码不能为空",
      type: "error"
    })
  }
  else if (addUserInfo.value['nickname'] === "") {
    ElNotification({
      title: "昵称不能为空",
      type: "error"
    })
  }
  else if (addUserInfo.value['role'] === "") {
    ElNotification({
      title: "角色不能为空",
      type: "error"
    })
  }
  else {
    let res = await add_user_by_admin(addUserInfo.value)
    if (res['code'] === 200) {
      ElNotification({
        title: "添加成功",
        type: "success"
      })
      addDrawer.value = false
    }
    else {
      ElNotification({
        title: "添加失败",
        type: "error"
      })
    }
  }
}
</script>

<template>
  <div class="user-option-card">
    <el-card header="用户操作">
      <el-button @click="handleAddUser">添加用户</el-button>
      <el-input
          v-model="username"
          placeholder="输入用户名"
          class="input-with-select"
      >
        <template #append>
          <el-button @click="handleSearch" :icon="Search"/>
        </template>
      </el-input>
    </el-card>
  </div>
  <el-drawer
      direction="rtl"
      title="添加用户"
      v-model="addDrawer">
    <el-form label-position="top">
      <el-form-item label="用户名">
        <el-input placeholder="请输入用户名" v-model="addUserInfo.username"></el-input>
      </el-form-item>
      <el-form-item label="昵称">
        <el-input placeholder="请输入昵称" v-model="addUserInfo.nickname"></el-input>
      </el-form-item>
      <el-form-item label="角色">
        <el-select v-model="addUserInfo.role" placeholder="请选择用户角色">
          <el-option label="管理员" value="3"></el-option>
          <el-option label="普通用户" value="1"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="password" placeholder="请输入密码" v-model="addUserInfo.password"></el-input>
      </el-form-item>
      <el-collapse>
        <el-collapse-item title="邮箱">
          <el-input v-model="addUserInfo.email"></el-input>
        </el-collapse-item>
        <el-collapse-item title="手机">
          <el-input v-model="addUserInfo.phone"></el-input>
        </el-collapse-item>
      </el-collapse>
    </el-form>
    <template #footer>
      <el-button @click="addDrawer=false">取 消</el-button>
      <el-button type="success" @click="add_user">确 定</el-button>
    </template>
  </el-drawer>

</template>

<style>
.user-option-card {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 0 auto;
  width: 100%;
  height: 100%;

  .el-button {
    margin-top: 10px;
    margin-bottom: 10px;
    width: 100%;
  }

}

.input-with-select .el-input-group__prepend {
  background-color: var(--el-fill-color-blank);
}
</style>