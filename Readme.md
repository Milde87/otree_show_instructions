# Instructions Overlay for oTree 5

This oTree template includes a feature that allows participants to revisit previous 
instructions through a popup overlay, providing a user-friendly way to access essential 
information while completing tasks.

## Setup
- Copy the provided ````popup-instructions.css```` file into your ````_static/global/css/```` folder.
- Copy the provided ````popup-instructions.js```` file into your ````_static/global/js/```` folder.

## Usage
### Create ````popup.html```` in the ```_static/global/``` Folder
This file provides the structure for the popup overlay and dynamically displays content based on the current task status.

```html
<style>
    .title_h2 {
      font-weight: 500;
      font-size: x-large;
    }
</style>

<div class="box" align="center">
	<a class="button" href="#popup1">Previous instructions</a>
</div>

<div id="popup1" class="overlay">
	<div class="popup">
        <div>
            <a class="close" href="#">&times;</a>
        </div>
        <h2 style="text-align: center !important;">
            Previous Instructions
        </h2>
		<div class="content">
            <h2 style="text-align: left !important;">Task</h2>
            <hr>
            {{ if status >= 1 }}
                {{ include 'Instructions/content/01Task.html' }}
            {{ endif }}
            {{ if status >= 2 }}
                {{ include 'Instructions/content/02Task.html' }}
            {{ endif }}
            {{ if status >= 3 }}
                {{ include 'Instructions/content/03Task.html' }}
            {{ endif }}

        </div>
	</div>
</div>
```

#### Key Features:

1. **Dynamic Content**:

    Based on the ````status```` variable, different instruction files are included dynamically. 
2. These files (e.g., ````01Task.html````, ````02Task.html````, ````03Task.html````) should be located in the ````Instructions/content/```` directory.

2. **Reusable Template**:
   
   The popup structure can be reused across the study by adjusting the ````status```` variable or included content.


### Integrate the Popup in a Template
To include the popup overlay in your page, use the following template structure:

```html
{{ block styles }}
    <link href="{{ static 'global/css/popup-instructions.css' }}" rel="stylesheet"/>
{{ endblock }}

{{ block scripts }}
    <script src="{{ static 'global/js/popup-instructions.js' }}"></script>
{{ endblock }}

{{ block title }}
    Instructions 1 <hr>
{{ endblock }}

{{ block content }}

    <!-- Popup button and overlay -->
    <div style="position: absolute; top: 30px; right: 30px">
      {{ include "_static/global/popup.html" with status=0 & popup=1 }}
    </div>
    
    <!-- Main instructions -->
    {{ include 'Instructions/content/01Task.html' with popup=0 }}
    {{ next_button }}

{{ endblock }}

```

#### Explanation:
1. **Styles Block**:

    - Includes the (````popup-instructions.css````) file to style the popup overlay.


2. **Scripts Block**:

    - Includes the (````popup-instructions.js````) file to manage the popup's functionality.


3. **Popup Placement**:

    - The popup is positioned in the top-right corner of the page:

        ```html
        <div style="position: absolute; top: 30px; right: 30px">
            {{ include "_static/global/popup.html" with status=0 & popup=1 }}
        </div>
        ```

   - The popup.html template is included dynamically with the variables:
       
     - status=0: Indicates that there are no prior instructions available for the participant to view in the popup.
     - popup=1: Marks this as an instance of the popup.


4. **Instruction Content**:
    - Displays the main instructions from ````01Task.html````:
        ```html
       {{ include 'Instructions/content/01Task.html' with popup=0 }}
        ```
    
   - The ```popup=0``` variable is used to distinguish the main instructions from the popup content. 
   It allows for the inclusion of additional information or modifications specific to the popup version of the 
   instructions, ensuring the content displayed in the popup can differ if necessary.

## Help
If you have any questions, please feel free to contact me via my [homepage](https://www.studies-services.de/en).
