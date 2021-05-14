<template>
  <div>
    <base-header class="pb-6 content__title content__title--calendar">
      <div class="row align-items-center py-4">
        <div class="col-lg-6 col-7">
          <h6 class="h2 text-white d-inline-block mb-0">{{ $route.name }}</h6>
          <nav aria-label="breadcrumb" class="d-none d-md-inline-block ml-md-4">
            <route-bread-crumb></route-bread-crumb>
          </nav>
        </div>
        <div class="col-lg-6 mt-3 mt-lg-0 text-lg-right">
          <a
            href="#"
            @click.prevent="prev"
            class="fullcalendar-btn-prev btn btn-sm btn-default"
          >
            <i class="fas fa-angle-left"></i>
          </a>
          <a
            href="#"
            @click.prevent="next"
            class="fullcalendar-btn-next btn btn-sm btn-default"
          >
            <i class="fas fa-angle-right"></i>
          </a>
          <base-button
            class="btn btn-sm btn-default"
            @click="changeView('dayGridMonth')"
          >
            Month
          </base-button>
          <base-button
            class="btn btn-sm btn-default"
            @click="changeView('dayGridWeek')"
          >
            Week
          </base-button>
          <base-button
            class="btn btn-sm btn-default"
            @click="changeView('timeGridDay')"
          >
            Day
          </base-button>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--6">
      <div class="row">
        <div class="col">
          <!-- Fullcalendar -->
          <div class="card card-calendar">
            <!-- Card header -->
            <div class="card-header">
              <!-- Title -->
              <h5 class="h3 mb-0">Calendar</h5>
            </div>
            <!-- Card body -->
            <div class="card-body p-0 card-calendar-body">
              <div id="fullCalendar"></div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <modal v-model:show="showAddModal" modal-classes="modal-secondary">
      <form class="new-event--form" @submit.prevent="saveEvent">
        <base-input
          name="title"
          label="Event title"
          placeholder="Event Title"
          v-model="model.title"
          input-classes="form-control-alternative new-event--title"
        >
        </base-input>
        <div class="form-group">
          <label class="form-control-label d-block mb-3">Status color</label>
          <div class="btn-group btn-group-toggle btn-group-colors event-tag">
            <label
              v-for="color in eventColors"
              :key="color"
              class="btn"
              :class="[color, { 'active focused': model.className === color }]"
            >
              <input
                v-model="model.className"
                type="radio"
                name="event-tag"
                :value="color"
                autocomplete="off"
              />
            </label>
          </div>
        </div>
        <input type="hidden" class="new-event--start" />
        <input type="hidden" class="new-event--end" />
      </form>

      <template v-slot:footer>
        <button
          type="submit"
          class="btn btn-primary new-event--add"
          @click="saveEvent"
        >
          Add event
        </button>
        <button
          type="button"
          class="btn btn-link ml-auto"
          @click="showAddModal = false"
        >
          Close
        </button>
      </template>
    </modal>

    <modal v-model:show="showEditModal" modal-classes="modal-secondary">
      <form class="edit-event--form" @submit.prevent="editEvent">
        <base-input
          name="title2"
          label="Event title"
          placeholder="Event Title"
          v-model="model.title"
          input-classes="form-control-alternative new-event--title"
        >
        </base-input>
        <div class="form-group">
          <label class="form-control-label d-block mb-3">Status color</label>
          <div class="btn-group btn-group-toggle btn-group-colors event-tag">
            <label
              v-for="color in eventColors"
              :key="color"
              class="btn"
              :class="[color, { 'active focused': model.className === color }]"
            >
              <input
                v-model="model.className"
                type="radio"
                name="event-tag"
                :value="color"
                autocomplete="off"
              />
            </label>
          </div>
        </div>
        <base-input name="textarea" label="Description">
          <textarea
            v-model="model.description"
            class="form-control form-control-alternative edit-event--description textarea-autosize"
            placeholder="Event Desctiption"
          >
          </textarea>
          <i class="form-group--bar"></i>
        </base-input>
        <input type="hidden" class="new-event--start" />
        <input type="hidden" class="new-event--end" />
      </form>

      <template v-slot:footer>
        <base-button
          native-type="submit"
          type="primary"
          class="new-event--add"
          @click="editEvent"
          >Update</base-button
        >
        <base-button type="danger" @click="deleteEvent">Delete</base-button>
        <base-button type="link" class="ml-auto" @click="showAddModal = false"
          >Close</base-button
        >
      </template>
    </modal>
  </div>
</template>
<script>
import Modal from "@/components/Modal";
import { Calendar } from "@fullcalendar/core";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
import timeGridDay from "@fullcalendar/timegrid";
import RouteBreadCrumb from "@/components/Breadcrumb/RouteBreadcrumb";

const today = new Date();
const y = today.getFullYear();
const m = today.getMonth();
const d = today.getDate();
var calendar;
export default {
  name: "calendar",
  components: {
    RouteBreadCrumb,
    Modal,
  },
  data() {
    return {
      events: [
        {
          title: "All Day Event",
          start: new Date(y, m, 1),
          className: "event-default",
        },
        {
          id: 999,
          title: "Repeating Event",
          start: new Date(y, m, d - 4, 6, 0),
          allDay: false,
          className: "event-green",
        },
        {
          id: 999,
          title: "Repeating Event",
          start: new Date(y, m, d + 3, 6, 0),
          allDay: false,
          className: "event-orange",
        },
        {
          title: "Meeting",
          start: new Date(y, m, d - 1, 10, 30),
          allDay: false,
          className: "event-green",
        },
        {
          title: "Lunch",
          start: new Date(y, m, d + 7, 12, 0),
          end: new Date(y, m, d + 7, 14, 0),
          allDay: false,
          className: "event-red",
        },
        {
          title: "Md-pro Launch",
          start: new Date(y, m, d - 2, 12, 0),
          allDay: true,
          className: "event-azure",
        },
        {
          title: "Birthday Party",
          start: new Date(y, m, d + 1, 19, 0),
          end: new Date(y, m, d + 1, 22, 30),
          allDay: false,
          className: "event-azure",
        },
        {
          title: "Click for Creative Tim",
          start: new Date(y, m, 21),
          end: new Date(y, m, 22),
          url: "http://www.creative-tim.com/",
          className: "event-orange",
        },
        {
          title: "Click for Google",
          start: new Date(y, m, 21),
          end: new Date(y, m, 22),
          url: "http://www.creative-tim.com/",
          className: "event-orange",
        },
      ],
      model: {
        title: "New event",
        className: "bg-default",
        description:
          "Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
        start: "",
        end: "",
      },
      showAddModal: false,
      showEditModal: false,
      eventColors: [
        "bg-info",
        "bg-orange",
        "bg-red",
        "bg-green",
        "bg-default",
        "bg-blue",
        "bg-purple",
        "bg-yellow",
      ],
    };
  },
  methods: {
    initCalendar() {
      var calendarEl = document.getElementById("fullCalendar");

      calendar = new Calendar(calendarEl, {
        plugins: [dayGridPlugin, timeGridDay, interactionPlugin],
        selectable: true,
        headerToolbar: false,
        select: () => {
          this.showAddModal = true;
          this.model.start = new Date(y, m, 21);
          this.model.end = new Date(y, m, 21);
        },
        eventClick: () => {
          this.model = {
            title: event.title,
            className: event.classNames ? event.classNames.join(" ") : "",
            start: event.start,
            end: event.end,
            description:
              "Nullam id dolor id nibh ultricies vehicula ut id elit. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.",
          };
          this.showEditModal = true;
        },
        events: this.events,
      });
      calendar.render();
    },
    changeView(newView) {
      calendar.changeView(newView);
      calendar.view.title;
    },
    next() {
      calendar.next();
    },
    prev() {
      calendar.prev();
    },
    saveEvent() {
      if (this.model.title) {
        let event = {
          ...this.model,
          allDay: true,
        };
        this.events.push(JSON.parse(JSON.stringify(event)));
        console.log(this.events);
        this.model = {
          title: "",
          eventColor: "bg-danger",
          start: "",
          end: "",
        };
      }
      this.showAddModal = false;
    },
    editEvent() {
      let index = this.events.findIndex((e) => e.title === this.model.title);
      if (index !== -1) {
        this.events.splice(index, 1, this.model);
      }
      this.showEditModal = false;
    },
    deleteEvent() {
      let index = this.events.findIndex((e) => e.title === this.model.title);
      if (index !== -1) {
        this.events.splice(index, 1);
      }
      this.showEditModal = false;
    },
  },
  mounted() {
    this.initCalendar();
  },
};
</script>
<style lang="scss">
@import "~@/assets/sass/core/vendors/fullcalendar";
</style>
