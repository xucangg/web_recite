<template>
    <div class="header_container">
		<div class='menu'>
			<div class="menu-a">
				<a class="menu-u" href="/">
					<div class="menu-s">
						<img src='../static/svg/learn.svg'/>
						<span class='menu-f'>学习</span>
					</div>
				</a>
			</div>
			<div class="menu-block"></div>
			<div class="menu-a">
				<a class="menu-u" href='/vocabulary'>	
					<div class="menu-s">
						<img src='../static/svg/words.svg'/>
						<span class="menu-f">词汇</span>
					</div>
				</a>
			</div>
			<div class="menu-block"></div>
			<div class="menu-a">
				<a class="menu-u" href='/model'>
					<div class="abc menu-s">
						<img src='../static/svg/model.svg'/>
						<span class='menu-f'>模式</span>
					</div>
				</a>
			</div>
			<div class="menu-block"></div>
			<div class="user menu-a">
				<el-dropdown>
						<span>
							<img class="avatar" src='../static/svg/avatar.jpg'>
						</span>
						<el-dropdown-menu v-if="userInfo.name">
							<el-dropdown-item style="pointer-events:none">
								<p>用户 :<span style="margin-left:5px">{{ userInfo.name }}</span></p>
							</el-dropdown-item>
							<el-dropdown-item>个人信息</el-dropdown-item>
							<a @click="view_wrong_words"><el-dropdown-item>错词查看</el-dropdown-item></a>
							<a @click="logout"><el-dropdown-item>退出登录</el-dropdown-item></a>
						</el-dropdown-menu>
						<el-dropdown-menu v-else>
							<a href="/register"><el-dropdown-item >注册</el-dropdown-item></a>
							<a href="/login"><el-dropdown-item>登入</el-dropdown-item></a>
						</el-dropdown-menu>
				</el-dropdown>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters } from 'vuex'
import cookie from '../static/js/cookie'
export default {
	computed:{
		...mapGetters({
			userInfo:'userInfo'
		})
	},
	
	methods:{
		logout(){
			cookie.delCookie('name')
			cookie.delCookie('token')
			this.$store.dispatch('setInfo')
			this.$router.push('/login')
		},

		view_wrong_words(){

		}
	}

}
</script>


<style>
    .header_container{
	background-color: #fff;
	border-bottom: 2px solid #e5e5e5;
    color: #afafaf;
    font-size: 17px;
    left: 0;
    position: fixed;
    right: 0;
    top: 0;
	height: 70px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
	z-index: 1;
	}
	.menu{
	flex-direction: row;
    margin: 0 auto;
    max-width: 1140px;
	position: relative;
    padding: 0 24px;
    display: flex;
    height: 100%;
	}
	.menu-a{
	display: flex;
	align-items: center;
	}
	.menu-u{
	text-decoration: none;
	background-color: transparent;
	}
	.menu-f{
	font-size: 15px;
    font-weight: 700;
    letter-spacing: .8px;
    text-transform: uppercase;
	padding-left: 0.2rem;
	}
	.menu-s{
	display: flex;
	align-items: center;
	}
	.menu-block{
	flex-grow: 1;
    height: 100%;
	}

	.login-button>span{
		color: #67c23a;
	}
	.avatar{
		border-radius: 98px;
		height: 36px;
		border-style: none;
	}


</style>