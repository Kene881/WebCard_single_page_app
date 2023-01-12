<template>
  <Header/>
  <Technologies/>
  <Works/>
  <Contact/>
  <Footer/>
</template>

<script>
import Header from './components/Header.vue';
import Technologies from './components/Technologies.vue';
import Works from './components/Works.vue';
import Contact from './components/Contact.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Header,
    Technologies,
    Works,
    Contact,
    Footer
}
}
</script>
