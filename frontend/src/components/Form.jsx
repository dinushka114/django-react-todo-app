import React from 'react'

const Form = () => {
    return (
        <form className="container-sm">
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Task</label>
                <input type="password" class="form-control" id="exampleInputPassword1" />
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    )
}

export default Form
