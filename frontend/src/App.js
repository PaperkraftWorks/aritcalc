import Login from './AdminLTE/components/Login'

function App() {
  return (
    <div>
        <div>
            <script src="https://cdn.jsdelivr.net/npm/admin-lte@3.2/dist/js/adminlte.min.js"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/admin-lte@3.2/dist/css/adminlte.min.css"></link>
        </div>
        {Login()}
    </div>

  )
};

export default App;
