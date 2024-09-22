import React, { StrictMode, useState } from 'react'
import { createRoot } from 'react-dom/client'
import {
    createBrowserRouter,
    RouterProvider,
    useLoaderData,
    useRouteError
} from "react-router-dom";


function App() {
    const data = useLoaderData();
    const [count, setCount] = useState(0)

    return (
        <>
            <div>
            </div>
            <h1>Vite + React</h1>
            <div className="card">
                <button onClick={() => setCount((count) => count + 1)}>
                    count is {count}
                </button>
                <p>
                    {JSON.stringify(data)}
                </p>
                <p>
                    Edit <code>src/App.tsx</code> and save to test HMR
                </p>
            </div>
            <p className="read-the-docs">
                Click on the Vite and React logos to learn more
            </p>
        </>
    )
}


createRoot(document.getElementById('root')!).render(
    <StrictMode>
        <RouterProvider router={createBrowserRouter([
            // https://reactrouter.com/en/main/start/tutorial#nested-routes
            {
                path: "/",
                element: <App />,
                loader: async () => fetch("/api/hello"),
                // errorElement: (() => <div>{JSON.stringify(useRouteError())}</div>)(),
            },
        ])} />
    </StrictMode>,
)