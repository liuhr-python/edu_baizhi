<template>
    <div class="footer">
        <ul>
             <li v-for="(nav, index) in nav_list" :key="index">
                        <a href="" v-if="nav.position==2" >{{nav.title}}</a>
                        <!--                项目外的连接        -->
                        <!--<span v-if="nav.is_site"><a :href="nav.link">{{nav.title}}</a></span>-->
                        <!--&lt;!&ndash;                本项目的路由        &ndash;&gt;-->
                        <!--<span v-else><router-link :to="nav.link">{{nav.title}}</router-link></span>-->
                    </li>
            <!--<li>关于我们</li>-->
            <!--<li>联系我们</li>-->
            <!--<li>百知教育</li>-->
            <!--<li>帮助中心</li>-->
            <!--<li>意见反馈</li>-->
            <!--<li>新手指南</li>-->
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data() {
            return {
                nav_list: []
            }
        },
        created() {
            this.get_nav()
        },
        methods: {

            // 获取导航栏的方法
            get_nav() {
                this.$axios({
                    url: this.$settings.HOST + "home/nav/",
                    methods: "get",
                }).then(response => {
                    this.nav_list = response.data;
                }).catch(error => {
                    console.log(error.response);
                })
            },
        }
    }
</script>

<style scoped>
    .footer {
        width: 100%;
        height: 128px;
        background: #25292e;
        color: #fff;
    }

    .footer ul {
        margin: 0 auto 16px;
        padding-top: 38px;
        width: 810px;
    }

    .footer ul li a{
        float: left;
        width: 112px;
        margin: 0 10px;
        text-align: center;
        font-size: 14px;
        color: azure;
    }

    .footer ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .footer p {
        text-align: center;
        font-size: 12px;
    }
</style>
