
const API_URL = "http://localhost:5000";

export async function postText(text: string): Promise<any> {
    const response = await fetch(API_URL + "/text", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text
        })
    });
    if (!response.ok) {
        throw new Error("Error POSTing text");
    }
    else {
        const responseJson = await response.json();
        return responseJson;
    }
}