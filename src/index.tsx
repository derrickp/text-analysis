
import "core-js";
import "whatwg-fetch"

import * as React from "react";
import * as ReactDOM from "react-dom";

import { App } from "./app";

const elem = document.getElementById("textapp");
ReactDOM.render(<App />, elem);