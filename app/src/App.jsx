import axios from "axios"
import { useState } from "react"

function App() {
  const [code,setCode] = useState({'text':""});
  const [output,setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const handleChange = (e) =>{
    setCode({
      ...code,
      [e.target.id]:e.target.value
    })
  }

  const handleSubmit = async()=>{
    setLoading(true);
    setOutput(""); // Limpia la salida anterior
    try{
      const req = await axios.post('https://compilador-4zp3.onrender.com/api/code',code);
      await setOutput(req.data.output);
    }catch (error){
      console.error("Error al enviar el código:", error);
      setOutput("Error al procesar la solicitud"); // Mensaje de error al usurio 
    }finally{
      setLoading(false);
    }
  }

  return (
      <>
      <div className="min-h-screen bg-[#1e1e1e] text-gray-200 p-6 font-mono">
        <div className="max-w-4xl mx-auto space-y-4">
          <h1 className="text-xl font-semibold text-[#d4d4d4]">MiniLang</h1>

          {/* Textarea de entrada*/}
          <textarea  
            id="text"
            onChange={handleChange}
            className="w-full h-48 bg-[#1e1e1e] text-[#d4d4d4] border border-[#3c3c3c]
                       rounded-md p-3 focus:outline-none focus:border-[#007acc]
                       placeholder-gray-500 resize-none shadow-inner"
            placeholder="Escribe algo aqui...">
          </textarea>

          {/* TEXTAREA SALIDA*/ }
          <textarea
            value={output}
            readOnly
            className="w-full h-48 bg-[#1e1e1e] text-[#9cdcfe] border border-[#3c3c3c]
                       rounded-md p-3 focus:outline-none resize-none shadow-inner"
          ></textarea>

          {/*BOTON*/}
          <button
            onClick={handleSubmit}
            disabled={loading}
            className={`px-4 py-2 rounded-md font-semibold transition
              ${loading
                ? 'bg-[#0e639c] opacity-60 cursor-not-allowed'
                : 'bg-[#0e639c] hover:bg-[#1177bb]'}
            `}>
              {loading ? 'Enviando...':'Enviar'}
            </button>
        </div>
      </div>
    </>

  )
}

export default App