<template>
  <div>
    <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <h1> Post a new Job </h1>
        <v-form @submit.prevent="submit" v-model="valide">
          <v-text-field
            v-model="title"
            :counter="20"
            label="title"
          ></v-text-field>

          <v-textarea
            v-model="description"
            label="Description"
          ></v-textarea>

          <v-text-field
            v-model="company_name"
            :counter="20"
            label="company name"
          ></v-text-field>

          <v-text-field
            v-model="company_url"
            :counter="100"
            label="company url"
          ></v-text-field>

          <v-btn type="submit">submit</v-btn>
        </v-form>

      </v-flex>
    </v-layout>
    </v-container>
  </div>
</template>

<script>

export default {
  name: 'about',
  data () {
    return {
      title: '',
      valid: true,
      description: '',
      company_name: '',
      company_url: ''
    }
  },
  methods: {
    submit () {
      if (this.title && this.description && this.company_name && this.company_url) {
        this.$http.post('/api/job_post', {title: this.title,
          description: this.description,
          company_name: this.company_name,
          company_url: this.company_url}).then((res) => {
          console.log('job saved')
          this.title = ''
          this.description = ''
          this.company_name = ''
          this.company_url = ''
          alert('job created')
          this.$router.push('/')
        })
      } else {
        alert('You need to fill all the fields...')
      }
    }
  }
}

</script>

<style>

</style>
