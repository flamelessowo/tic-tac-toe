const App = {
    data() {

    },
    methods: {
        setCheck(event) {
            event.target.innerHTML = "X";
        }
    }

}

const app = Vue.createApp(App);

app.mount('#app');
