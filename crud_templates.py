
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>Project TimeSheet Details</h2>

  <table class="table">
    <thead class="table-dark">
      <tr>
        <th>SN</th>
        <th>Project Name</th>
        <th>Client</th>
        <th>Hours</th>
        <th>Description</th>
        <th>Update</th>
        <th>Delete</th>
      </tr>
    </thead>
    <tbody>
        {% for project in projects %}
          {% if project.project_name == 'Ola' %}
              <tr class="table-warning">
                <td>{{ project.id }}</td>
                <td>{{ project.project_name }}</td>
                <td>{{ project.client }}</td>
                <td>{{ project.hours }}</td>
                <td>{{ project.description }}</td>
                <td><a href="/crud/update/{{ project.id }}/"><span class="glyphicon glyphicon-trash"></span>Update</a></td>
                <td><a href="/crud/delete/{{ project.id }}/"><span class="glyphicon glyphicon-trash"></span>Delete</a></td>
              </tr>
          {% endif %}
          {% if project.project_name == 'Yulu' %}
              <tr class="table-danger">
                <td>{{ project.id }}</td>
                <td>{{ project.project_name }}</td>
                <td>{{ project.client }}</td>
                <td>{{ project.hours }}</td>
                <td>{{ project.description }}</td>
                <td><a href="/crud/update/{{ project.id }}/"><span class="glyphicon glyphicon-trash"></span>Update</a></td>
                <td><a href="/crud/delete/{{ project.id }}/"><span class="glyphicon glyphicon-trash"></span>Delete</a></td>
              </tr>
          {% endif %}
          {% if project.project_name == 'Uber' %}
              <tr class="table-danger">
                <td>{{ project.id }}</td>
                <td>{{ project.project_name }}</td>
                <td>{{ project.client }}</td>
                <td>{{ project.hours }}</td>
                <td>{{ project.description }}</td>
                <td><a href="/crud/update/{{ project.id }}/"><span class="glyphicon glyphicon-trash"></span>Update</a></td>
                <td><a href="/crud/delete/{{ project.id }}/"><span class="glyphicon glyphicon-trash"></span>Delete</a></td>
              </tr>
          {% endif %}
        {% endfor %}
    </tbody>
  </table>
</div>

</body>
</html>
