<template>
  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex xs12>
        <v-img
          src="https://www.futurejobs.io/assets/future-jobs-58355e7746a94c63711a3bdd18221deb9f252f553d04c6bcdcc8309de1e12fab.png"
          class="my-3"
          contain
          height="150"
        ></v-img>
      </v-flex>

      <v-flex mb-4>
        <p class="display-1 font-weight-bold mb-3">
          The best machine learning, AI, and data science jobs, in one place.
        </p>
        <p class="subheading font-weight-regular">
          Future Jobs is the best place to find and list jobs that power the future.
        </p>
        <v-btn
          color="#00AFFF"
          to="/post_job"
          >
          Post a job for $299
        </v-btn>
         <v-divider />
      </v-flex>

      <v-flex
        mb-5
        xs12
      >

        <v-list subheader>
          <v-subheader>
            Recent jobs
            <v-switch
              v-model="activate"
              label="edit mode"
            ></v-switch>
          </v-subheader>
          <div v-for="item in items"
            :key="item.title"
            >
            <v-list-tile>

              <v-list-tile-content>
                <div>
                  <span class="bold">{{item.company_name}} - </span>
                  <a :href="item.company_url">{{item.title}}</a>
                  <v-btn icon @click="setJob(item, 'edit')" v-if="activate">
                    <v-icon color='success'>edit</v-icon>
                  </v-btn>
                  <v-btn icon @click="setJob(item, 'delete')" v-if="activate">
                    <v-icon color='error'>cancel</v-icon>
                  </v-btn>
                </div>

              </v-list-tile-content>

              <v-list-tile-action>
                <v-list-tile-title> {{item.created_date}} </v-list-tile-title>
              </v-list-tile-action>
            </v-list-tile>

            <v-divider></v-divider>
          </div>

        </v-list>

        <v-dialog v-model="edit" v-if="job" persistent max-width="600px">
          <v-card>
            <v-card-title>
              <span class="headline">edit job</span>
            </v-card-title>
            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex md12>

                    <v-form @submit.prevent="submitEdit">
                      <v-text-field
                        v-model="job.title"
                        :counter="20"
                        label="title"
                      ></v-text-field>

                      <v-textarea
                        v-model="job.description"
                        label="Description"
                      ></v-textarea>

                      <v-text-field
                        v-model="job.company_name"
                        :counter="20"
                        label="company name"
                      ></v-text-field>

                      <v-text-field
                        v-model="job.company_url"
                        :counter="100"
                        label="company url"
                      ></v-text-field>

                      <v-btn type="submit">submit</v-btn>
                    </v-form>

                  </v-flex>

                </v-layout>
              </v-container>
            </v-card-text>
          </v-card>
        </v-dialog>

        <v-dialog v-model="remove" v-if="job" persistent max-width="290">
          <v-card>
            <v-card-text></v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" flat @click="remove = false">Close</v-btn>
              <v-btn color="red darken-1" flat @click="deleteJob">Delete Job</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
  mounted () {
    this.loadData()
  },
  data: () => ({
    items: [],
    edit: false,
    on: false,
    job: false,
    remove: false,
    activate: true
  }),
  methods: {
    loadData () {
      this.$http.get('/api/job_post').then((res) => {
        this.items = res.data
      })
    },
    setJob (job, _type) {
      this.job = job
      if (_type === 'edit') {
        this.edit = true
      } else {
        this.remove = true
      }
    },
    submitEdit () {
      if (this.job.title && this.job.description && this.job.company_name && this.job.company_url) {
        this.$http.put('/api/job_post', {id: this.job.id,
          title: this.job.title,
          description: this.job.description,
          company_name: this.job.company_name,
          company_url: this.job.company_url}).then((res) => {
          console.log('job saved')
          this.edit = false
          this.job = false
        })
      } else {
        alert('You need to fill all the fields...')
      }
    },
    deleteJob () {
      this.$http.delete('/api/job_post', {id: this.job.id}).then((res) => {
        this.loadData()
        this.remove = false
        alert('job deleted')
      })
    }
  }
}
</script>

<style>
.bold {
  font-weight: bold;
}

</style>
