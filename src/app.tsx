import * as React from "react";

import { postText } from "./server";

export interface AppProps {}
export interface AppState {
    textResponse: any;
    text: string;
}

export class App extends React.Component<AppProps, AppState> {

    constructor(props: AppProps) {
        super(props);
        this.state = {
            textResponse: undefined,
            text: ""
        };
        this.sendText = this.sendText.bind(this);
        this.textChanged = this.textChanged.bind(this);
    }

    textChanged(event: React.SyntheticEvent<HTMLTextAreaElement>) {
        this.setState({ text: event.currentTarget.value });
    }

    async sendText() {
        await this.setTextResponse("Loading...");
        const json = await postText(this.state.text);
        const textResponse = JSON.stringify(json, null, 2);
        await this.setTextResponse(textResponse);
    }

    setTextResponse(textResponse: string): Promise<void> {
        return new Promise((resolve, reject) => {
            this.setState({ textResponse }, () => {
                resolve();
            });
        });
    }

    render() {
        return (
            <div>
                <div>
                    Put some text in the area below, click send and see some stats about it!
                </div>
                <div>
                    <textarea onChange={this.textChanged} value={this.state.text}>

                    </textarea>
                </div>
                <button onClick={this.sendText}>Send Text</button>
                <div><pre>{this.state.textResponse}</pre></div>
            </div>
        )
    }
}