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
				<a class="menu-u" href='/#/vocabulary'>	
					<el-dropdown>
					<div class="menu-s">
						<img src='../static/svg/words.svg'/>
						<span class="menu-f">词汇</span>
					</div>
						<el-dropdown-menu>
							<el-dropdown-item>CTE-4</el-dropdown-item>
							<el-dropdown-item>CTE-6</el-dropdown-item>				
						</el-dropdown-menu>
					</el-dropdown>
				</a>
			</div>
			<div class="menu-block"></div>
			<div class="menu-a">
				<a class="menu-u" href='/#/model'>
					<div class="abc menu-s">
						<img src='../static/svg/model.svg'/>
						<span class='menu-f'>模式</span>
					</div>
				</a>
			</div>
			<div class="menu-block"></div>
			<div class="user menu-a">
				<el-dropdown>
					<el-avatar ></el-avatar>
						<el-dropdown-menu>
							<el-dropdown-item>信息</el-dropdown-item>
							<el-dropdown-item>登出</el-dropdown-item>
						</el-dropdown-menu>
				</el-dropdown>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	data(){
		return {
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
	

</style>






















