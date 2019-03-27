<template>
  <v-app>
    <v-toolbar app color="#EEF6F6">
      <v-toolbar-title class="headline text-uppercase">
        <router-link to="/">
          <span>Future</span>
          <span class="font-weight-light"> Jobs</span>
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        flat
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2"></span>
      </v-btn>
    </v-toolbar>

    <v-content>
       <router-view/>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      //
    }
  }
}
</script>
